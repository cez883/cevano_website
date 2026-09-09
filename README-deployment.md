# Cevano IT Solutions — Deployment & Handover Guide

**Architecture: GitHub → Cloudflare Pages → cevano.co.uk, with Cloudflare DNS,
Resend for the contact form, and Microsoft 365 as the sole email provider.**

This is a full rewrite of the deployment guide following the move away from
Hostinger/PHP shared hosting to a static, serverless architecture. If you're
looking for the old Hostinger instructions, they no longer apply — this
document supersedes them entirely.

---

## 1. Project overview

This is the production website for Cevano IT Solutions: a static HTML/CSS/JS
site (English + Polish) with one small serverless function handling the
contact form. There is no database, no CMS, no build step, and — as of this
migration — no PHP and no traditional web server.

```
cevano-site/
├── index.html, services.html, about.html, contact.html, 404.html   ← English pages
├── pl/                                                              ← Polish pages (mirrors the above)
│   ├── index.html, services.html, about.html, contact.html
│   └── legal/privacy-policy.html, legal/terms.html
├── legal/
│   ├── privacy-policy.html
│   └── terms.html
├── css/style.css                 ← all styling (light + dark theme)
├── js/main.js                    ← theme toggle, mobile nav, cookie banner,
│                                    contact form, scroll reveal, mini-nav
├── assets/img/                   ← logo, favicons, social-share image
├── functions/
│   └── api/
│       └── contact.js            ← Cloudflare Pages Function (contact form)
├── _headers                      ← Cloudflare Pages security/caching headers
├── _redirects                    ← Cloudflare Pages redirect rules (www canonical)
├── robots.txt
├── sitemap.xml
├── site.webmanifest
├── .gitignore
└── build*.py, build.py           ← Python scripts used to generate the HTML
                                     (development tool only — see §14)
```

---

## 2. Final architecture

```
                 ┌──────────────────────┐
   Local dev  →  │   GitHub (private)   │
                 └──────────┬───────────┘
                             │ git push to main
                             ▼
                 ┌──────────────────────┐
                 │  Cloudflare Pages    │  ← auto-deploys on every push
                 │  (static hosting)    │
                 └──────────┬───────────┘
                             │
                             ▼
GoDaddy (registrar) ──DNS──▶ Cloudflare DNS ──▶ https://www.cevano.co.uk

Contact form:

  contact.html / pl/contact.html
          │  fetch() POST
          ▼
  functions/api/contact.js   (Cloudflare Pages Function)
          │  REST API call, server-side secret
          ▼
  Resend (transactional email API)
          │  sends email
          ▼
  enquiries@cevano.co.uk
          │
          ▼
  Microsoft 365 / Exchange Online  ← where the mailbox actually lives
```

**What changed from the old Hostinger setup:**

| Before (Hostinger) | Now (Cloudflare) |
|---|---|
| Apache + `.htaccess` | Cloudflare edge network + `_headers` / `_redirects` |
| PHP `contact-handler.php` + `mail()` | `functions/api/contact.js` (Pages Function) + Resend API |
| FTP/File Manager upload | `git push` → automatic deployment |
| SPF/DKIM set up *for Hostinger's mail* | Not needed — Hostinger email is gone entirely |
| Manual DNS at GoDaddy | DNS managed at Cloudflare (GoDaddy stays the registrar) |

**What did NOT change:** the visual design, page content, English/Polish
versions, all URLs (still `.html` paths, e.g. `/services.html`), SEO
metadata, and Microsoft 365 as your email provider — nothing about
`enquiries@cevano.co.uk` or its DNS records is touched by this migration.

---

## 3. GitHub setup

1. Create a **private** GitHub repository (e.g. `cevano-website`).
2. From the project folder, initialise and push:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Cevano IT Solutions website"
   git branch -M main
   git remote add origin https://github.com/<your-username>/cevano-website.git
   git push -u origin main
   ```
3. Check `.gitignore` (included) is doing its job — run `git status` before
   your first commit and confirm nothing like `.dev.vars` or `.env` is
   listed as staged. **No API keys or secrets should ever be committed.**

From here on, GitHub's `main` branch is the source of truth: every push to
`main` triggers a new Cloudflare Pages deployment automatically (§13).

---

## 4. Cloudflare account setup

1. Create a free Cloudflare account at cloudflare.com if you don't already
   have one (many people also use Cloudflare for DNS only — if you do, you
   can reuse that same account).
2. You'll need two things configured under this account before deploying:
   - A **Cloudflare Pages** project (§5)
   - **Cloudflare DNS** for cevano.co.uk (§9)

---

## 5. Cloudflare Pages deployment

1. In the Cloudflare dashboard, go to **Workers & Pages → Create → Pages →
   Connect to Git**.
2. Select your `cevano-website` GitHub repository (you'll be asked to
   authorise Cloudflare's GitHub app — scope it to this one repo if you're
   offered the choice).
3. Configure the build settings exactly as follows:

   | Setting | Value |
   |---|---|
   | Framework preset | **None** |
   | Build command | *(leave empty)* |
   | Build output directory | `/` (root of the repo) |
   | Root directory | `/` (unless you nested the site in a subfolder) |

   This is a plain static site with no build step — Cloudflare deploys the
   repo contents as-is, and picks up `_headers`, `_redirects`, and the
   `functions/` folder automatically.
4. Click **Save and Deploy**. The first deployment runs immediately and
   gives you a temporary URL like `cevano-website.pages.dev` — use this to
   test everything (§12) before connecting the real domain.

---

## 6. Environment variables and secrets

Set these in **Cloudflare Pages → your project → Settings → Environment
variables**, applied to the **Production** environment (and Preview, if you
want contact-form testing to work on preview deployments too).

| Name | Type | Required | Value |
|---|---|---|---|
| `RESEND_API_KEY` | **Secret** | Yes | Your Resend API key (§7) |
| `TO_EMAIL` | Plain text | No | Defaults to `enquiries@cevano.co.uk` — only set this if enquiries should go somewhere else |
| `FROM_EMAIL` | Plain text | No | `"Cevano Website <forms@notifications.cevano.co.uk>"` once you've verified a sending subdomain in Resend (§7). Defaults to Resend's shared testing domain if not set. |
| `TURNSTILE_SECRET_KEY` | **Secret** | No | Only if you enable Cloudflare Turnstile (§16) |

**Never** put any of these values directly in the code or commit them to
GitHub — always use Cloudflare's environment variable UI (or
`wrangler pages secret put <NAME>` if you're using the CLI). Mark
`RESEND_API_KEY` and `TURNSTILE_SECRET_KEY` as **Secret** (not plain text) so
they're encrypted and never shown again in the dashboard after saving.

After adding or changing environment variables, **redeploy** (Cloudflare
Pages → Deployments → retry latest, or just push a new commit) for the
Function to pick them up.

---

## 7. Transactional email provider: Resend

**Why Resend:** a generous free tier (3,000 emails/month, 100/day —
comfortably enough for a small business contact form), a simple REST API
that needs no SDK or npm dependency (the Function just uses `fetch()`),
solid deliverability, and one of the most commonly recommended providers for
exactly this Cloudflare Pages Functions use case. It's also completely
independent of Microsoft 365 — it just sends *to* your M365 mailbox, the
same as any external sender would.

**Setup:**

1. Create a free account at resend.com.
2. Go to **API Keys → Create API Key**, name it something like
   `cevano-website-contact-form`, and restrict it to **Sending access** only
   (not full account access). Copy the key immediately — you won't see it
   again.
3. Add this as the `RESEND_API_KEY` secret in Cloudflare Pages (§6).

**Sending domain — two options:**

- **Quick start (testing only):** leave `FROM_EMAIL` unset. The Function
  defaults to Resend's own shared domain (`onboarding@resend.dev`), which
  works immediately with zero DNS setup — fine for confirming everything
  works end-to-end, but not ideal for production (generic sender address,
  weaker deliverability reputation).
- **Recommended for production:** verify a **subdomain** you control in
  Resend, e.g. `notifications.cevano.co.uk`. In Resend, go to **Domains →
  Add Domain**, enter `notifications.cevano.co.uk` (not the bare
  `cevano.co.uk`), and Resend gives you a small set of DNS records
  (SPF/TXT, DKIM/CNAME) to add.

  **This is the important part for you:** because these records are scoped
  to the `notifications.` subdomain, they live entirely separately from your
  root domain's existing Microsoft 365 SPF/DKIM/MX records — no overlap,
  nothing to merge or conflict-check. Full detail in §10.

  Once verified, set `FROM_EMAIL` to something like:
  `"Cevano Website <forms@notifications.cevano.co.uk>"`

---

## 8. Connecting the custom domain

Once DNS is on Cloudflare (§9) and the first Pages deployment is live:

1. In **Cloudflare Pages → your project → Custom domains → Set up a custom
   domain**, add `www.cevano.co.uk` (the canonical version used throughout
   the site's SEO metadata — see the note in `_redirects`).
2. Also add the bare `cevano.co.uk` apex domain as a second custom domain.
3. Cloudflare automatically creates the right DNS records for both (since
   DNS is already on Cloudflare, this is a one-click step, not manual
   record entry).
4. The `_redirects` file already included in this project 301-redirects
   `cevano.co.uk` → `www.cevano.co.uk`, so both work but only one is
   canonical for search engines.

---

## 9. Moving DNS from GoDaddy to Cloudflare

The domain **stays registered at GoDaddy** — you're only moving DNS
*management* to Cloudflare, not the registration itself.

1. In Cloudflare, go to **Add a Site**, enter `cevano.co.uk`, and select the
   Free plan.
2. Cloudflare scans your domain's existing DNS records and shows you a
   list — **review this list carefully before continuing** (see §10 for
   exactly what to check).
3. Cloudflare gives you two nameservers, e.g. `ns1.cloudflare.com` /
   `ns2.cloudflare.com` (yours will be specific to your account).
4. Log in to **GoDaddy → My Products → Domains → DNS** for cevano.co.uk, and
   change the nameservers from GoDaddy's defaults to the two Cloudflare
   nameservers.
5. Save. Propagation typically takes anywhere from a few minutes up to 24
   hours. Cloudflare emails you once the switch is detected.

⚠️ **Do this deliberately, not casually** — until you've completed §10's
checklist, don't remove or "clean up" any existing DNS records that
Cloudflare imported. Extra/unused records can be deleted later; a missing
MX or SPF record can break your email immediately.

---

## 10. Preserving Microsoft 365 email — critical checklist

This is the step most likely to cause real damage if rushed, so treat it as
its own checklist, separate from the general DNS move above.

**Before switching nameservers**, log into the Microsoft 365 admin center →
**Settings → Domains → cevano.co.uk → DNS records**, and note down every
record listed there. You're typically looking for something like:

| Type | Purpose | Example (yours will differ) |
|---|---|---|
| MX | Routes incoming mail to Exchange Online | `cevano-co-uk.mail.protection.outlook.com` |
| TXT (SPF) | Authorises Microsoft 365 to send as your domain | `v=spf1 include:spf.protection.outlook.com -all` |
| CNAME × 2 | DKIM signing keys | `selector1._domainkey`, `selector2._domainkey` |
| CNAME | Autodiscover (for Outlook client setup) | `autodiscover.cevano.co.uk` |
| TXT (optional) | DMARC policy, if configured | `_dmarc.cevano.co.uk` |

**After Cloudflare imports your DNS records** (step 2 in §9), verify every
one of the above is present and unchanged in the Cloudflare DNS dashboard.
Cloudflare's import scan is generally reliable, but manually cross-check
against your Microsoft 365 admin center list — don't assume.

**Adding the Resend records (§7) will NOT conflict**, because:
- Resend's records live on a subdomain (`notifications.cevano.co.uk`), not
  the root domain — a completely separate DNS namespace from your M365 SPF/
  DKIM records on the apex.
- If you ever *did* need an SPF record on the exact same hostname as an
  existing one, SPF requires merging into a single record (multiple SPF TXT
  records on one hostname breaks SPF checks) — but since Resend's subdomain
  approach avoids this entirely, there's nothing to merge for this setup.

**One more thing to check:** Cloudflare's proxy (the orange cloud icon) only
applies to A/AAAA/CNAME records for *web* traffic — it should be set to
**DNS only (grey cloud)** for MX records and any mail-related CNAME/TXT
records, since proxying doesn't apply to mail routing. Cloudflare defaults
MX records to DNS-only automatically, but it's worth a quick visual check.

**Final verification after the nameserver switch propagates:** send a test
email to `enquiries@cevano.co.uk` from an external address (e.g. Gmail) and
confirm it arrives normally in Outlook/Exchange Online, exactly as before.

---

## 11. SSL configuration

Cloudflare Pages provisions and renews SSL certificates automatically for
both the `.pages.dev` URL and any custom domains you attach — nothing to
manually configure. Under **Cloudflare → SSL/TLS**, the recommended mode for
a Pages project is **Full (strict)**, typically the default. HTTPS
redirects are automatic; the "force HTTPS" rule that used to live in
`.htaccess` isn't needed anymore.

---

## 12. Contact form testing

Test on the `*.pages.dev` preview URL first, then again on the live domain
once connected.

1. **English form** (`/contact.html`): submit with a real email address you
   can check, filling every field. Confirm:
   - The success message appears inline (no page reload)
   - The email arrives at `enquiries@cevano.co.uk` in Outlook
   - **Reply-To** is set to the address you submitted (hit reply and check)
   - The email body includes name, company, email, phone, service, language
     (EN), and message
2. **Polish form** (`/pl/contact.html`): repeat the above, confirm
   `Language: PL` appears in the email and the on-page success/error
   messages are in Polish.
3. **Validation:** try submitting with an empty required field, an invalid
   email, and without ticking consent — confirm each shows an inline error
   without sending an email.
4. **Honeypot:** hard to test manually by design, but you can confirm the
   hidden field exists by viewing page source and checking for
   `name="company_website"` inside the form.
5. **No-JS fallback (optional but good to confirm once):** disable
   JavaScript in your browser, submit the form, and confirm you're
   redirected back to the contact page with a visible confirmation message
   (via the `?sent=1` query parameter).

---

## 13. Deployment workflow

Once connected, this is the whole day-to-day workflow:

```
Edit files locally
      ↓
git add . && git commit -m "..."
      ↓
git push origin main
      ↓
Cloudflare Pages detects the push automatically
      ↓
Builds and deploys within ~1 minute
      ↓
Live at www.cevano.co.uk
```

No manual upload step, ever. Every push to `main` is a production
deployment. If you want a staging/review step before something goes live,
push to a different branch first and open a pull request — Cloudflare Pages
automatically builds a **preview URL** for every branch/PR, so you can
check changes before merging to `main`.

---

## 14. About the Python build scripts (`build.py` / `build_*.py`)

**Recommendation: keep them.** These scripts generate the HTML pages from
shared templates (header, footer, navigation, language switcher) so a
sitewide change — updating the footer, adding a nav link, editing the
company address — happens once in `build.py` and regenerates all 16 pages
consistently, instead of hand-editing every English and Polish page
separately (where mistakes creep in on bilingual sites, as happened a few
times during earlier development of this project).

**They are development tooling only** — Cloudflare Pages does not run
Python, does not know these files exist, and does not need them at deploy
time. It only ever deploys the static HTML/CSS/JS/Function files already
sitting in the repo. Nothing about the Cloudflare Pages "Build command"
setting (§5, left empty) invokes them.

**To make a sitewide content change:**
```bash
# edit build.py or the relevant build_*.py file, then:
python3 build_home.py
python3 build_services.py
python3 build_about.py
python3 build_contact.py
python3 build_legal.py
python3 build_404.py
# then commit and push the regenerated HTML files as usual
```

If you'd eventually prefer not to maintain a Python toolchain, a template
system built into a static site generator (Eleventy, Astro, etc.) is the
natural next step — but given the site's current size (16 pages, no rapid
growth planned), the existing scripts are simple, dependency-free, and easy
for any future developer to read top to bottom in a few minutes, so a
migration isn't necessary right now.

---

## 15. Privacy / GDPR review

The Privacy & Cookie Policy (`/legal/privacy-policy.html` and
`/pl/legal/privacy-policy.html`) has been updated to reflect the new
architecture:

- **Cloudflare** is now listed as the hosting/infrastructure provider
- **Resend** is now listed as the transactional email processor for the
  contact form
- **Microsoft 365 / Exchange Online** is listed as where the
  `enquiries@cevano.co.uk` mailbox actually lives
- **IP address collection has been removed** from the contact form email
  itself — the old PHP handler included the submitter's IP address in the
  notification email; the new Cloudflare Function does not, since it wasn't
  being used for anything and minimising collected data is better practice.
  The policy now accurately notes that Cloudflare, as infrastructure,
  handles standard connection data as part of normal web operation, but
  Cevano itself doesn't separately collect or store it.

**Remaining placeholders you still need to complete** (flagged with a
yellow "Placeholder" badge on both legal pages):

- Date the Privacy Policy and Terms & Conditions were last published/updated
- VAT number, if applicable (company number and registered address are
  already filled in with the details you provided)
- Confirmation of whether any analytics service is in use — the Cookies
  section currently flags this as unconfirmed; if you're not running any
  analytics, this can simply be changed to say so

No other data collection has been invented or assumed — the policy only
describes what the site and contact form actually do.

---

## 16. Security review summary

A basic review appropriate for a small business site, not an
over-engineered enterprise setup:

- **Input validation:** all contact form fields are validated server-side
  in `functions/api/contact.js` (required fields, email format, consent) —
  never trusting client-side validation alone.
- **Spam protection:** honeypot field + a client-side time-trap (rejects
  submissions faster than 2.5 seconds) are active by default with no setup
  required. **Cloudflare Turnstile** is supported and recommended as an
  additional layer if spam becomes a problem — see below for why it's not
  force-enabled by default.
- **Secrets:** `RESEND_API_KEY` and (if used) `TURNSTILE_SECRET_KEY` are
  stored as encrypted Cloudflare secrets, never in code or in GitHub. The
  Function runs server-side, so the API key is never exposed to the browser.
- **Security headers:** `_headers` sets `X-Content-Type-Options`,
  `X-Frame-Options`, `Referrer-Policy`, and a conservative
  `Permissions-Policy` on every route.
- **HTTPS:** enforced automatically by Cloudflare for every route, no
  configuration needed.
- **CORS:** not applicable — the contact form only ever calls `/api/contact`
  on the same origin (relative URL), so there's no cross-origin request to
  configure or restrict.
- **Rate limiting:** not separately configured. Cloudflare's platform-level
  DDoS protection applies automatically to every Pages project; combined
  with the honeypot/time-trap (and optional Turnstile), this is a
  proportionate level of protection for a small business contact form. If
  spam volume becomes a real problem later, Cloudflare's rate limiting
  rules (available even on the free plan in limited form) are the natural
  next step.

### Should you enable Cloudflare Turnstile?

**Recommendation: worth adding if/when spam becomes an actual problem — not
required to launch.** The honeypot + time-trap combination catches the
overwhelming majority of automated spam bots with zero friction for real
visitors. Turnstile adds meaningfully stronger protection against more
sophisticated bots, and since you're already on Cloudflare, it's free and
well-integrated. The trade-off is one more moving part and a small amount
of visual footprint on the form.

`functions/api/contact.js` already has full support built in — if
`TURNSTILE_SECRET_KEY` is set, verification is enforced; if left unset,
Turnstile is skipped entirely and the form works exactly as shipped.

**To enable it later:**
1. In Cloudflare dashboard → **Turnstile → Add site**, register
   `cevano.co.uk`, choose the "Managed" widget type, and copy the **Site
   Key** and **Secret Key**.
2. Set `TURNSTILE_SECRET_KEY` as a Cloudflare Pages secret (§6).
3. Add the widget script and div to both `contact.html` and
   `pl/contact.html`, inside the `<form>` element, just above the submit
   button:
   ```html
   <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
   <div class="cf-turnstile" data-sitekey="YOUR_SITE_KEY_HERE"></div>
   ```
   No JavaScript changes are needed — Turnstile automatically injects its
   response token into the form, and `functions/api/contact.js` already
   reads it.

---

## 17. Pre-launch checklist

- [ ] Push the project to a private GitHub repository (§3)
- [ ] Create the Cloudflare Pages project and confirm the `.pages.dev`
      preview deploys successfully with no build errors (§5)
- [ ] Add `RESEND_API_KEY` as a Cloudflare Pages secret (§6, §7)
- [ ] Send a test enquiry through the form on the `.pages.dev` URL and
      confirm it arrives at `enquiries@cevano.co.uk` (§12)
- [ ] Move DNS to Cloudflare, carefully preserving every Microsoft 365
      record (§9, §10)
- [ ] Attach both `cevano.co.uk` and `www.cevano.co.uk` as custom domains
      on the Pages project (§8)
- [ ] Confirm SSL is active (padlock shows) on the live domain (§11)
- [ ] Re-test the contact form (both languages) on the live domain, not
      just the preview URL (§12)
- [ ] Send a test email to `enquiries@cevano.co.uk` from an external
      address and confirm normal Microsoft 365 delivery, unaffected by the
      DNS move (§10)
- [ ] Verify a sending subdomain in Resend and set `FROM_EMAIL` for
      production-quality deliverability, rather than the shared testing
      domain (§7)
- [ ] Fill in the remaining legal-page placeholders (§15)
- [ ] Spot-check the site on a real phone: mobile menu, dark mode toggle,
      language switcher, contact form

## 18. Post-launch SEO checklist

- [ ] Submit `https://www.cevano.co.uk/sitemap.xml` to Google Search Console
- [ ] Submit the same sitemap to Bing Webmaster Tools
- [ ] Confirm `robots.txt` is reachable at
      `https://www.cevano.co.uk/robots.txt`
- [ ] Spot-check a few pages with Google's Rich Results Test to confirm the
      `ProfessionalService` structured data is read correctly
- [ ] Confirm the `www` vs. apex redirect (§8) is working both ways before
      search engines crawl both — a working 301 avoids duplicate-content
      issues from day one

---

## 19. Rollback procedure

Because Cloudflare Pages keeps every previous deployment:

1. Go to **Cloudflare Pages → your project → Deployments**.
2. Find the last known-good deployment in the list.
3. Click the **⋯** menu → **Rollback to this deployment**.

This instantly repoints production to that build — no git revert or new
push required, though it's good practice to also fix and re-push the
underlying issue in git so the next deploy doesn't reintroduce it.

For a git-level rollback instead: `git revert <bad-commit>` and push — this
triggers a normal new deployment from the reverted state.

---

## 20. Troubleshooting

**Contact form returns a generic error / nothing happens:**
- Check **Cloudflare Pages → your project → Functions → Real-time Logs**
  (or `wrangler pages deployment tail`) while submitting a test enquiry —
  the Function logs the exact error (e.g. a Resend API failure) to console.
- Confirm `RESEND_API_KEY` is set for the **Production** environment
  specifically, not only Preview.
- Confirm you redeployed after adding/changing environment variables (§6).

**Emails aren't arriving at all:**
- Check the Resend dashboard's **Logs** tab — it shows every send attempt
  and whether it succeeded, bounced, or was rejected.
- If using a verified sending subdomain, confirm its DNS records show as
  "Verified" (not "Pending") in Resend.
- Check the Microsoft 365 mailbox's spam/junk folder as a first step.

**Emails arrive but deliverability seems poor / lands in spam:**
- This usually means you're still on Resend's shared `resend.dev` sending
  domain — verify your own subdomain (§7) for a real sender reputation.

**Microsoft 365 email stopped working after the DNS move:**
- Immediately check Cloudflare DNS against your original Microsoft 365 DNS
  record list (§10) — an MX, SPF, or DKIM record was likely missed during
  the Cloudflare import and needs to be added back manually.
- This is why §10 exists as a dedicated checklist — always verify before
  and after the nameserver switch, not just once.

**Site shows old content after pushing to GitHub:**
- Check **Cloudflare Pages → Deployments** to confirm a new deployment
  actually triggered and succeeded — if the push didn't reach `main` (e.g.
  pushed to a different branch), no production deploy happens.
- Hard-refresh / clear browser cache — `_headers` sets long cache lifetimes
  for CSS/JS/images, great for performance but meaning a browser that
  already cached the old version may need a forced refresh.

**A page 404s that shouldn't:**
- Cloudflare Pages serves files by their exact path — `/about.html` must be
  requested as written; there's no automatic `.html` stripping. Confirm
  links in the HTML match actual filenames exactly (the project's link
  structure already accounts for this throughout).

**Turnstile widget doesn't appear / verification always fails:**
- Confirm the site key in the HTML matches the one shown in the Cloudflare
  Turnstile dashboard for this exact domain.
- Confirm `TURNSTILE_SECRET_KEY` (the *secret* key, not the site key) is
  set as a Cloudflare Pages environment variable.
