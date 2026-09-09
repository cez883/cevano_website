(function () {
  "use strict";

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

    /* ---------- Cookie consent banner ---------- */
    var cookieBanner = document.querySelector("[data-cookie-banner]");
    if (cookieBanner) {
      var consent = null;
      try { consent = localStorage.getItem("cevano-cookie-consent"); } catch (e) {}
      if (!consent) {
        cookieBanner.classList.add("visible");
      }
      cookieBanner.querySelectorAll("[data-cookie-accept], [data-cookie-dismiss]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          try { localStorage.setItem("cevano-cookie-consent", "1"); } catch (e) {}
          cookieBanner.classList.remove("visible");
        });
      });
    }

    /* ---------- Scroll reveal ---------- */
    var prefersReducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (window.IntersectionObserver && !prefersReducedMotion) {
      var revealTargets = document.querySelectorAll(
        ".section-head, .service-grid, .subservice-grid, .why-grid, .cta-banner, " +
        ".about-layout, .detail-grid, .process-grid, .form-card, .contact-info, .legal-content"
      );
      var revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1, rootMargin: "0px 0px -60px 0px" });

      revealTargets.forEach(function (el) {
        el.classList.add("reveal");
        revealObserver.observe(el);
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
        var scrollPos = window.scrollY + 140;
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

      // Handle the no-JS-navigation fallback: contact-handler.php redirects
      // back here with ?sent=1 or ?error=1 when a full page POST happened.
      var params = new URLSearchParams(window.location.search);
      if (params.has("sent")) {
        showStatus(true);
      } else if (params.has("error")) {
        showStatus(false);
      }

      form.addEventListener("submit", function (e) {
        // Basic honeypot + time-trap spam check (real validation also happens server-side)
        var honeypot = form.querySelector('[name="company_website"]');
        var tooFast = Date.now() - startTime < 2500;

        if ((honeypot && honeypot.value) || tooFast) {
          e.preventDefault();
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
              showStatus(true);
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

      function showStatus(success) {
        if (!status) return;
        status.className = "form-status " + (success ? "success" : "error");
        status.textContent = success
          ? (form.dataset.successMsg || "Thank you. Your enquiry has been sent successfully. We'll be in touch as soon as possible.")
          : (form.dataset.errorMsg || "Sorry, something went wrong sending your message. Please email us directly instead.");
        status.setAttribute("role", "status");
        status.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    }
  });
})();
