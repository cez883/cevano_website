(function () {
  "use strict";

  /* ---------- Google Analytics (tylko po zgodzie) ---------- */
  var GA_MEASUREMENT_ID = "G-N0N6N3TM8P";          // usługa "Cevano IT Solutions" w GA
  var CONSENT_KEY = "cevano-analytics-consent";      // zapis decyzji w localStorage
  var CONSENT_MAX_AGE_MS = 365 * 24 * 3600 * 1000;   // decyzja ważna 12 miesięcy
  var gaLoaded = false;

  // Zwraca "granted", "denied" albo null (brak decyzji / decyzja starsza niż 12 miesięcy)
  function readAnalyticsConsent() {
    try {
      // Stary klucz ze starego banera (tylko niezbędne cookies) — już nie jest zgodą na analitykę
      localStorage.removeItem("cevano-cookie-consent");
      var saved = JSON.parse(localStorage.getItem(CONSENT_KEY) || "null");
      if (!saved || (saved.choice !== "granted" && saved.choice !== "denied")) return null;
      if (Date.now() - saved.time > CONSENT_MAX_AGE_MS) return null;
      return saved.choice;
    } catch (e) { return null; }
  }

  function saveAnalyticsConsent(choice) {
    try { localStorage.setItem(CONSENT_KEY, JSON.stringify({ choice: choice, time: Date.now() })); } catch (e) {}
  }

  // Ładuje gtag.js tylko na prawdziwej domenie (nie na podglądzie *.pages.dev ani lokalnie)
  function loadGoogleAnalytics() {
    if (gaLoaded) return;
    if (!/(^|\.)cevano\.co\.uk$/.test(window.location.hostname)) return;
    gaLoaded = true;
    window["ga-disable-" + GA_MEASUREMENT_ID] = false;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA_MEASUREMENT_ID, {
      allow_google_signals: false,               // bez Google signals
      allow_ad_personalization_signals: false,   // bez reklam
      cookie_expires: 13 * 30 * 24 * 3600        // cookies _ga ok. 13 miesięcy
    });
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_MEASUREMENT_ID;
    document.head.appendChild(s);
  }

  // Po "Reject": wyłącza GA na tej stronie i usuwa cookies _ga*
  function disableGoogleAnalytics() {
    window["ga-disable-" + GA_MEASUREMENT_ID] = true;
    var host = window.location.hostname;
    var domains = ["", host, "." + host, ".cevano.co.uk"];
    document.cookie.split(";").forEach(function (c) {
      var name = c.split("=")[0].trim();
      if (name.indexOf("_ga") !== 0) return;
      domains.forEach(function (d) {
        document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + (d ? "; domain=" + d : "");
      });
    });
  }

  /* ---------- Theme (light/dark) ---------- */
  var root = document.documentElement;
  var stored = null;
  try { stored = localStorage.getItem("cevano-theme"); } catch (e) {}
  if (stored === "dark" || stored === "light") {
    root.setAttribute("data-theme", stored);
  } else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
    root.setAttribute("data-theme", "dark");
  }

  function currentTheme() {
    return root.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }

  document.addEventListener("DOMContentLoaded", function () {
    var toggles = document.querySelectorAll("[data-theme-toggle]");
    toggles.forEach(function (btn) {
      btn.setAttribute("aria-pressed", currentTheme() === "dark");
      btn.addEventListener("click", function () {
        var next = currentTheme() === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        try { localStorage.setItem("cevano-theme", next); } catch (e) {}
        toggles.forEach(function (t) { t.setAttribute("aria-pressed", next === "dark"); });
      });
    });

    /* ---------- Mobile nav ---------- */
    var navToggle = document.querySelector("[data-nav-toggle]");
    if (navToggle) {
      navToggle.addEventListener("click", function () {
        var open = root.getAttribute("data-nav-open") === "true";
        root.setAttribute("data-nav-open", open ? "false" : "true");
        navToggle.setAttribute("aria-expanded", open ? "false" : "true");
      });
    }
    document.querySelectorAll(".main-nav a").forEach(function (link) {
      link.addEventListener("click", function () {
        root.setAttribute("data-nav-open", "false");
        if (navToggle) navToggle.setAttribute("aria-expanded", "false");
      });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && root.getAttribute("data-nav-open") === "true") {
        root.setAttribute("data-nav-open", "false");
        if (navToggle) { navToggle.setAttribute("aria-expanded", "false"); navToggle.focus(); }
      }
    });

    /* ---------- Cookie consent banner + Google Analytics ---------- */
    // Google Analytics ładuje się WYŁĄCZNIE po kliknięciu "Accept analytics"
    // (PECR / UK GDPR). "Reject" wyłącza GA i usuwa jego cookies.
    // Decyzja jest pamiętana 12 miesięcy, potem pytamy ponownie.
    // "Cookie settings" w stopce pokazuje baner ponownie.
    var cookieBanner = document.querySelector("[data-cookie-banner]");
    if (cookieBanner) {
      var choice = readAnalyticsConsent();
      if (choice === "granted") {
        loadGoogleAnalytics();
      } else if (choice === null) {
        cookieBanner.classList.add("visible");
      }
      var acceptBtn = cookieBanner.querySelector("[data-cookie-accept]");
      var rejectBtn = cookieBanner.querySelector("[data-cookie-reject]");
      if (acceptBtn) acceptBtn.addEventListener("click", function () {
        saveAnalyticsConsent("granted");
        cookieBanner.classList.remove("visible");
        loadGoogleAnalytics();
      });
      if (rejectBtn) rejectBtn.addEventListener("click", function () {
        saveAnalyticsConsent("denied");
        cookieBanner.classList.remove("visible");
        disableGoogleAnalytics();
      });
      document.querySelectorAll("[data-cookie-settings]").forEach(function (link) {
        link.addEventListener("click", function (e) {
          e.preventDefault();
          cookieBanner.classList.add("visible");
        });
      });
    }

    /* ---------- Gentle entrance for blocks below the fold ----------
       Content is never hidden: .js-enter only marks a block, and .in-view
       plays a short rise as it scrolls into view. If the observer never
       fires, the block simply stays as it is, fully visible. */
    var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (window.IntersectionObserver && !reduceMotion) {
      var enterTargets = Array.prototype.filter.call(
        document.querySelectorAll(".section-head, .service-card, .subservice-card, .problem-grid, .review-offer, .process-step, .cta-banner"),
        function (el) { return el.getBoundingClientRect().top > window.innerHeight; }
      );
      var enterObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            enterObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.15 });
      enterTargets.forEach(function (el) {
        el.classList.add("js-enter");
        enterObserver.observe(el);
      });
    }

    /* ---------- Services mini-nav: active section on scroll ---------- */
    var miniNav = document.querySelector("[data-mini-nav]");
    if (miniNav) {
      var miniLinks = Array.prototype.slice.call(miniNav.querySelectorAll("a"));
      var targets = miniLinks
        .map(function (link) {
          var id = link.getAttribute("href").split("#")[1];
          return id ? document.getElementById(id) : null;
        })
        .filter(Boolean);

      function setActiveMiniLink() {
        // Same offset the CSS scroll-margin uses: sticky header + this sub-nav.
        var header = document.querySelector(".site-header");
        var offset = (header ? header.offsetHeight : 0) + miniNav.offsetHeight + 24;
        var scrollPos = window.scrollY + offset;
        var current = targets[0];
        targets.forEach(function (t) {
          if (t.offsetTop <= scrollPos) current = t;
        });
        miniLinks.forEach(function (link) {
          var isCurrent = current && link.getAttribute("href").split("#")[1] === current.id;
          link.classList.toggle("is-active", isCurrent);
        });
      }
      if (targets.length) {
        setActiveMiniLink();
        window.addEventListener("scroll", setActiveMiniLink, { passive: true });
      }
    }

    /* ---------- Contact form (progressive enhancement) ---------- */
    var form = document.querySelector("[data-contact-form]");
    if (form) {
      var status = form.querySelector("[data-form-status]");
      var submitBtn = form.querySelector("[data-form-submit]");
      var startTime = Date.now();

      var done = document.querySelector("[data-form-done]");

      // Handle the no-JS-navigation fallback: functions/api/contact.js redirects
      // back here with ?sent=1 or ?error=1 when a full page POST happened.
      var params = new URLSearchParams(window.location.search);
      if (params.has("sent")) {
        showDone("", "");
      } else if (params.has("error")) {
        showStatus(false);
      }

      // Pre-select the service when arriving from a service page (?service=m365).
      // Only known keys map to an option; anything else is ignored.
      var SERVICE_KEYS = {
        "m365": "Microsoft 365",
        "website": "Website / landing page",
        "it-support": "IT Support",
        "data": "Data Analytics / Power BI"
      };
      var serviceSelect = form.querySelector('[name="service"]');
      var wanted = SERVICE_KEYS[params.get("service")];
      if (serviceSelect && wanted) {
        for (var i = 0; i < serviceSelect.options.length; i++) {
          if (serviceSelect.options[i].value === wanted) { serviceSelect.selectedIndex = i; break; }
        }
      }

      form.addEventListener("submit", function (e) {
        // Basic honeypot + time-trap spam check (real validation also happens server-side)
        var honeypot = form.querySelector('[name="company_website"]');
        var tooFast = Date.now() - startTime < 2500;

        if (honeypot && honeypot.value) {
          e.preventDefault();
          return;
        }
        if (tooFast) {
          // Real people who autofill and submit instantly get told what to do
          // instead of a button that silently does nothing.
          e.preventDefault();
          showNotice(form.dataset.tooFast || "Please wait a moment, then press Send again.");
          return;
        }

        // Submit via fetch so we can show an inline success message without
        // leaving the page (progressive enhancement — see the no-JS
        // fallback note below for what happens if this fails/is unavailable).
        var action = form.getAttribute("action") || "/api/contact";

        if (window.fetch) {
          e.preventDefault();
          if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = form.dataset.sending || "Sending..."; }

          fetch(action, {
            method: "POST",
            body: new FormData(form),
            headers: { "Accept": "application/json" }
          }).then(function (res) {
            if (res.ok) {
              var emailField = form.querySelector('[name="email"]');
              var messageField = form.querySelector('[name="message"]');
              showDone(emailField ? emailField.value.trim() : "", messageField ? messageField.value.trim() : "");
              form.reset();
              startTime = Date.now();
            } else {
              showStatus(false);
            }
          }).catch(function () {
            showStatus(false);
          }).finally(function () {
            if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = form.dataset.submitLabel || "Send enquiry"; }
          });
        }
        // If fetch isn't available (very old browsers), let the form submit
        // normally — functions/api/contact.js detects the non-JSON request
        // and responds with a redirect back to this page (?sent=1 / ?error=1),
        // which the code above picks up on load to show the same message.
      });

      function showNotice(text) {
        if (!status) return;
        status.className = "form-status error";
        status.textContent = text;
        status.setAttribute("role", "alert");
      }

      // Success: swap the form for a confirmation panel that repeats the
      // visitor's email and message, so nothing they wrote disappears.
      function showDone(email, message) {
        if (!done) { showStatus(true, email); return; }
        var withEmail = done.querySelector("[data-done-with-email]");
        var noEmail = done.querySelector("[data-done-no-email]");
        var emailSlot = done.querySelector("[data-done-email]");
        var copyWrap = done.querySelector("[data-done-copy-wrap]");
        var copy = done.querySelector("[data-done-copy]");
        if (email && emailSlot) {
          emailSlot.textContent = email;
          withEmail.hidden = false; noEmail.hidden = true;
        } else if (withEmail) {
          withEmail.hidden = true; noEmail.hidden = false;
        }
        if (message && copy) {
          copy.textContent = message;
          copyWrap.hidden = false;
        } else if (copyWrap) {
          copyWrap.hidden = true;
        }
        if (status) { status.className = "form-status"; status.textContent = ""; }
        form.hidden = true;
        done.hidden = false;
        var heading = done.querySelector("[data-done-heading]");
        if (heading) heading.focus();
        done.scrollIntoView({ behavior: "smooth", block: "start" });
      }

      if (done) {
        var again = done.querySelector("[data-done-again]");
        if (again) again.addEventListener("click", function () {
          done.hidden = true;
          form.hidden = false;
          // Drop ?sent=1 so a reload shows the empty form, not the old confirmation.
          if (window.history && history.replaceState && params.has("sent")) {
            params.delete("sent");
            var q = params.toString();
            history.replaceState(null, "", window.location.pathname + (q ? "?" + q : "") + window.location.hash);
          }
          startTime = Date.now();
          var first = form.querySelector('[name="name"]');
          if (first) first.focus();
        });
      }

      function showStatus(success, email) {
        if (!status) return;
        status.className = "form-status " + (success ? "success" : "error");
        status.textContent = "";
        if (success) {
          var msg = (email && form.dataset.successEmailMsg)
            ? form.dataset.successEmailMsg.replace("{email}", email)
            : (form.dataset.successMsg || "Thank you, your enquiry has been sent.");
          status.textContent = msg;
        } else {
          // Error text ends with a real mailto link so the visitor has a way out.
          status.appendChild(document.createTextNode((form.dataset.errorMsg || "Sorry, your enquiry couldn't be sent. Please email us at") + " "));
          var link = document.createElement("a");
          link.href = "mailto:enquiries@cevano.co.uk";
          link.textContent = "enquiries@cevano.co.uk";
          status.appendChild(link);
          status.appendChild(document.createTextNode("."));
        }
        status.setAttribute("role", success ? "status" : "alert");
        status.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    }
  });
})();
