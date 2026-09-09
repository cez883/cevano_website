/**
 * Cevano IT Solutions — contact form handler (Cloudflare Pages Function).
 *
 * Route: POST /api/contact
 * Replaces the old PHP handler (contact-handler.php / PHP mail()) used on
 * Hostinger. This runs as a Cloudflare Pages Function (serverless, no PHP,
 * no traditional hosting) and sends enquiries via the Resend transactional
 * email API to enquiries@cevano.co.uk (Microsoft 365 / Exchange Online).
 *
 * Required environment variable / secret (set in Cloudflare Pages dashboard
 * or via `wrangler pages secret put`, NEVER committed to git):
 *
 *   RESEND_API_KEY        Resend API key (secret)
 *
 * Optional environment variables:
 *
 *   TO_EMAIL               Destination inbox. Defaults to enquiries@cevano.co.uk
 *   FROM_EMAIL              "Display Name <address@domain>" the mail is sent
 *                           from. Must be on a domain verified in Resend.
 *                           Defaults to Resend's shared sending domain, which
 *                           works immediately but is fine for testing only —
 *                           see README-deployment.md for verifying your own
 *                           subdomain for production sending.
 *   TURNSTILE_SECRET_KEY    If set, Cloudflare Turnstile verification is
 *                           enforced (see README for enabling the widget).
 *                           If unset, Turnstile is skipped entirely and the
 *                           form relies on the honeypot + time-trap checks
 *                           below — a reasonable default for a small
 *                           business contact form.
 *
 * This file intentionally has zero npm dependencies — it calls Resend's
 * plain REST API with fetch(), keeping the project dependency-free and easy
 * to audit.
 */

const DEFAULT_TO = "enquiries@cevano.co.uk";
const DEFAULT_FROM = "Cevano Website <onboarding@resend.dev>";

export async function onRequestPost(context) {
  const { request, env } = context;

  let data;
  try {
    const contentType = request.headers.get("content-type") || "";
    if (contentType.includes("application/json")) {
      data = await request.json();
    } else {
      const form = await request.formData();
      data = Object.fromEntries(form.entries());
    }
  } catch (err) {
    return respond(request, false, "Sorry, we couldn't read your submission. Please try again.", 400, "en");
  }

  const lang = data._lang === "pl" ? "pl" : "en";

  // ---- Spam protection: honeypot field must be empty ----
  if (data.company_website) {
    // Pretend success so bots don't learn the honeypot worked.
    return respond(request, true, "OK", 200, lang);
  }

  // ---- Optional Cloudflare Turnstile verification ----
  if (env.TURNSTILE_SECRET_KEY) {
    const token = data["cf-turnstile-response"];
    if (!token) {
      return respond(request, false, "Please complete the verification check and try again.", 400, lang);
    }
    try {
      const verifyRes = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          secret: env.TURNSTILE_SECRET_KEY,
          response: token,
          remoteip: request.headers.get("CF-Connecting-IP") || undefined,
        }),
      });
      const verifyJson = await verifyRes.json();
      if (!verifyJson.success) {
        return respond(request, false, "Verification failed. Please try again.", 400, lang);
      }
    } catch (err) {
      // Fail closed on verification errors — safer default for a public form.
      return respond(request, false, "Verification check failed. Please try again.", 400, lang);
    }
  }

  // ---- Field validation (mirrors the old PHP handler's rules) ----
  const name = clean(data.name);
  const company = clean(data.company);
  const phone = clean(data.phone);
  const email = clean(data.email);
  const service = clean(data.service);
  const message = typeof data.message === "string" ? data.message.trim() : "";
  const consent = data.consent === "on" || data.consent === "true" || data.consent === true;

  const errors = [];
  if (!name) errors.push(lang === "pl" ? "Imię i nazwisko jest wymagane." : "Name is required.");
  if (!email || !isValidEmail(email)) errors.push(lang === "pl" ? "Wymagany jest prawidłowy adres e-mail." : "A valid email is required.");
  if (!message) errors.push(lang === "pl" ? "Wiadomość jest wymagana." : "Message is required.");
  if (!consent) errors.push(lang === "pl" ? "Zgoda jest wymagana." : "Consent is required.");

  if (errors.length) {
    return respond(request, false, errors.join(" "), 400, lang);
  }

  const toAddress = env.TO_EMAIL || DEFAULT_TO;
  const fromAddress = env.FROM_EMAIL || DEFAULT_FROM;
  const submittedAt = new Date().toISOString();

  const subject = `New enquiry from cevano.co.uk${service ? " — " + service : ""}`;
  const textBody = [
    "New enquiry received via the Cevano website contact form.",
    "",
    `Name: ${name}`,
    `Company: ${company || "(not provided)"}`,
    `Email: ${email}`,
    `Phone: ${phone || "(not provided)"}`,
    `Service / area of support: ${service || "(not specified)"}`,
    `Language: ${lang.toUpperCase()}`,
    "",
    "Message:",
    message,
    "",
    "---",
    `Submitted: ${submittedAt}`,
  ].join("\n");

  try {
    const emailRes = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: fromAddress,
        to: [toAddress],
        reply_to: email,
        subject,
        text: textBody,
      }),
    });

    if (!emailRes.ok) {
      const errText = await emailRes.text();
      console.error("Resend API error:", emailRes.status, errText);
      return respond(
        request, false,
        lang === "pl"
          ? "Niestety wystąpił problem podczas wysyłania wiadomości. Napisz do nas bezpośrednio na enquiries@cevano.co.uk."
          : "Sorry, the message could not be sent. Please try again or email us directly.",
        502, lang
      );
    }
  } catch (err) {
    console.error("Contact handler fetch error:", err);
    return respond(
      request, false,
      lang === "pl"
        ? "Niestety wystąpił problem podczas wysyłania wiadomości. Spróbuj ponownie."
        : "Sorry, something went wrong sending your message. Please try again.",
      500, lang
    );
  }

  return respond(
    request, true,
    lang === "pl"
      ? "Dziękujemy. Twoje zapytanie zostało wysłane. Odezwiemy się najszybciej jak to możliwe."
      : "Thank you. Your enquiry has been sent successfully.",
    200, lang
  );
}

// Reject non-POST methods explicitly (Pages Functions only route matching
// export names, but this keeps behaviour explicit and easy to reason about).
export async function onRequestGet() {
  return new Response("Method not allowed", { status: 405 });
}

/* ---------------- helpers ---------------- */

function clean(value) {
  if (value === undefined || value === null) return "";
  return String(value).trim().replace(/[\r\n]+/g, " ");
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

/**
 * Returns JSON for fetch()-based submissions (the normal path — see
 * js/main.js), or a 302 redirect back to the contact page with a ?sent=1 /
 * ?error=1 flag for the rare no-JavaScript fallback case, mirroring the
 * behaviour of the old PHP handler.
 */
function respond(request, success, message, status, lang) {
  const accept = request.headers.get("Accept") || "";
  const xrw = request.headers.get("X-Requested-With") || "";
  const wantsJson = accept.includes("application/json") || xrw.toLowerCase() === "xmlhttprequest";

  if (wantsJson) {
    return new Response(JSON.stringify({ success, message }), {
      status,
      headers: { "Content-Type": "application/json" },
    });
  }

  const base = lang === "pl" ? "/pl/contact.html" : "/contact.html";
  const url = new URL(request.url);
  const redirectTo = `${url.origin}${base}${success ? "?sent=1" : "?error=1"}`;
  return Response.redirect(redirectTo, 303);
}
