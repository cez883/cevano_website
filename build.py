#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for Cevano IT Solutions.
Produces plain HTML/CSS/JS files ready for Hostinger — no build step needed
at runtime; this script is only a development-time convenience.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://www.cevano.co.uk"

# ------------------------------------------------------------------
# Icons (inline SVG, currentColor / CSS vars so they theme automatically)
# ------------------------------------------------------------------
ICON_SUN = '''<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'''
ICON_MOON = '''<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>'''
ICON_MENU = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'''
ICON_CHECK = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'''

THEME_INIT_SCRIPT = '''<script>(function(){try{var t=localStorage.getItem("cevano-theme");if(t==="dark"||t==="light"){document.documentElement.setAttribute("data-theme",t);}else if(window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches){document.documentElement.setAttribute("data-theme","dark");}}catch(e){}})();</script>'''

# ------------------------------------------------------------------
# Translation strings shared across header/footer/forms
# ------------------------------------------------------------------
T = {
    "en": {
        "nav_home": "Home", "nav_services": "Services", "nav_about": "About", "nav_contact": "Contact",
        "cta_get_in_touch": "Get in touch", "cta_our_services": "Our services", "cta_email_us": "Email us",
        "skip": "Skip to main content",
        "footer_tagline": "Practical IT support, Microsoft 365 management and data analytics for small businesses across Northamptonshire and beyond.",
        "footer_company": "Company", "footer_services": "Services", "footer_legal": "Legal",
        "footer_privacy": "Privacy Policy", "footer_terms": "Terms & Conditions",
        "footer_rights": "All rights reserved.",
        "lang_name": "EN", "alt_lang_name": "PL",
        "theme_label": "Toggle dark mode",
        "menu_label": "Menu",
        "cookie_text": "We use a small number of essential and analytics cookies to help this website work reliably and to understand how it's used. See our Privacy &amp; Cookie Policy for details.",
        "cookie_accept": "Accept",
        "cookie_dismiss": "Dismiss",
    },
    "pl": {
        "nav_home": "Strona główna", "nav_services": "Usługi", "nav_about": "O nas", "nav_contact": "Kontakt",
        "cta_get_in_touch": "Skontaktuj się", "cta_our_services": "Nasze usługi", "cta_email_us": "Napisz do nas",
        "skip": "Przejdź do treści głównej",
        "footer_tagline": "Praktyczne wsparcie IT, zarządzanie Microsoft 365 i analiza danych dla małych firm w Northamptonshire i okolicach.",
        "footer_company": "Firma", "footer_services": "Usługi", "footer_legal": "Informacje prawne",
        "footer_privacy": "Polityka prywatności", "footer_terms": "Regulamin",
        "footer_rights": "Wszelkie prawa zastrzeżone.",
        "lang_name": "PL", "alt_lang_name": "EN",
        "theme_label": "Przełącz tryb ciemny",
        "menu_label": "Menu",
        "cookie_text": "Używamy niewielkiej liczby niezbędnych plików cookie oraz plików analitycznych, aby strona działała prawidłowo i abyśmy mogli rozumieć, jak jest wykorzystywana. Szczegóły znajdziesz w naszej Polityce prywatności i&nbsp;cookies.",
        "cookie_accept": "Akceptuję",
        "cookie_dismiss": "Zamknij",
    }
}

def head(lang, asset_prefix, title, description, canonical_path, alt_canonical_path, og_image_path):
    """canonical_path e.g. '' for home, 'services.html', 'legal/privacy-policy.html' (relative to lang root, no leading slash).
    asset_prefix is the relative path from the current file back to the SITE root (where /css, /js, /assets live)."""
    en_root = SITE_URL + "/"
    pl_root = SITE_URL + "/pl/"
    if lang == "en":
        this_url = en_root + canonical_path
        alt_url = pl_root + alt_canonical_path
    else:
        this_url = pl_root + canonical_path
        alt_url = en_root + alt_canonical_path
    hreflang_other = "pl" if lang == "en" else "en"
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{this_url}">
<link rel="alternate" hreflang="{lang}" href="{this_url}">
<link rel="alternate" hreflang="{hreflang_other}" href="{alt_url}">
<link rel="alternate" hreflang="x-default" href="{en_root}{canonical_path if lang=='en' else alt_canonical_path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cevano IT Solutions">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{this_url}">
<meta property="og:image" content="{SITE_URL}/{og_image_path}">
<meta property="og:locale" content="{'en_GB' if lang=='en' else 'pl_PL'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{asset_prefix}assets/img/favicon-32.png" sizes="32x32">
<link rel="icon" href="{asset_prefix}assets/img/favicon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="{asset_prefix}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{asset_prefix}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{asset_prefix}css/style.css">
{THEME_INIT_SCRIPT}
</head>
'''

def header_html(lang, lang_prefix, asset_prefix, active, alt_href):
    """lang_prefix: relative path from current file back to its OWN language root (pl/ or site root).
    asset_prefix: relative path from current file back to the SITE root (css/js/assets)."""
    t = T[lang]
    def nav_item(key, href):
        cur = ' aria-current="page"' if active == key else ''
        return f'<li><a href="{href}"{cur}>{t["nav_"+key]}</a></li>'
    home_href = lang_prefix + "index.html"
    services_href = lang_prefix + "services.html"
    about_href = lang_prefix + "about.html"
    contact_href = lang_prefix + "contact.html"

    other_lang_label = t["alt_lang_name"]
    this_lang_label = t["lang_name"]
    if lang == "en":
        lang_switch = f'''<div class="lang-switch" aria-label="Language switch">
          <a href="{home_href}" aria-current="true">{this_lang_label}</a><span>|</span><a href="{alt_href}">{other_lang_label}</a>
        </div>'''
    else:
        lang_switch = f'''<div class="lang-switch" aria-label="Language switch">
          <a href="{alt_href}">{other_lang_label}</a><span>|</span><a href="{home_href}" aria-current="true">{this_lang_label}</a>
        </div>'''

    logo_path = asset_prefix + "assets/img/logo-trimmed.png"
    logo_webp = asset_prefix + "assets/img/logo-trimmed.webp"
    logo_white_path = asset_prefix + "assets/img/logo-white.png"
    logo_white_webp = asset_prefix + "assets/img/logo-white.webp"
    return f'''<a class="skip-link" href="#main">{t['skip']}</a>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="{home_href}" aria-label="Cevano IT Solutions — home">
      <picture class="logo-light">
        <source srcset="{logo_webp}" type="image/webp">
        <img src="{logo_path}" alt="Cevano IT Solutions" width="195" height="120">
      </picture>
      <picture class="logo-dark">
        <source srcset="{logo_white_webp}" type="image/webp">
        <img src="{logo_white_path}" alt="Cevano IT Solutions" width="192" height="120">
      </picture>
    </a>
    <nav class="main-nav" aria-label="Primary">
      <ul class="nav-links">
        {nav_item('home', home_href)}
        {nav_item('services', services_href)}
        {nav_item('about', about_href)}
        {nav_item('contact', contact_href)}
      </ul>
      <div class="header-actions">
        {lang_switch}
        <button type="button" class="theme-toggle" data-theme-toggle aria-label="{t['theme_label']}" aria-pressed="false">
          {ICON_MOON}{ICON_SUN}
        </button>
        <a class="btn btn-primary btn-sm" href="{contact_href}">{t['cta_get_in_touch']}</a>
      </div>
    </nav>
    <button type="button" class="nav-toggle" data-nav-toggle aria-label="{t['menu_label']}" aria-expanded="false">
      {ICON_MENU}
    </button>
  </div>
</header>
'''

def footer_html(lang, lang_prefix, asset_prefix):
    t = T[lang]
    home_href = lang_prefix + "index.html"
    services_href = lang_prefix + "services.html"
    about_href = lang_prefix + "about.html"
    contact_href = lang_prefix + "contact.html"
    privacy_href = lang_prefix + "legal/privacy-policy.html"
    terms_href = lang_prefix + "legal/terms.html"
    logo_path = asset_prefix + "assets/img/logo-white.png"
    logo_webp = asset_prefix + "assets/img/logo-white.webp"
    year = "2026"
    company_no_label = "Company No." if lang == "en" else "Numer firmy"
    if lang == "en":
        services_items = [
            (services_href + "#it-support", "IT Support"),
            (services_href + "#microsoft-365", "Microsoft 365"),
            (services_href + "#data-analytics", "Data Analytics &amp; Power BI"),
        ]
    else:
        services_items = [
            (services_href + "#it-support", "Wsparcie IT"),
            (services_href + "#microsoft-365", "Microsoft 365"),
            (services_href + "#data-analytics", "Analiza danych i Power BI"),
        ]
    services_li = "\n".join(f'<li><a href="{h}">{lbl}</a></li>' for h, lbl in services_items)
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <picture>
        <source srcset="{logo_webp}" type="image/webp">
        <img src="{logo_path}" alt="Cevano IT Solutions" width="176" height="110" loading="lazy">
      </picture>
      <p>{t['footer_tagline']}</p>
      <p class="company-meta">
        {company_no_label} 17428300<br>
        1 Gresham Drive, West Hunsbury<br>
        Northampton, NN4 9SB
      </p>
    </div>
    <div class="footer-col">
      <h4>{t['footer_company']}</h4>
      <ul>
        <li><a href="{home_href}">{t['nav_home']}</a></li>
        <li><a href="{about_href}">{t['nav_about']}</a></li>
        <li><a href="{contact_href}">{t['nav_contact']}</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>{t['footer_services']}</h4>
      <ul>
        {services_li}
      </ul>
    </div>
    <div class="footer-col">
      <h4>{t['footer_legal']}</h4>
      <ul>
        <li><a href="{privacy_href}">{t['footer_privacy']}</a></li>
        <li><a href="{terms_href}">{t['footer_terms']}</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; {year} Cevano IT Solutions. {t['footer_rights']}</span>
    <div class="footer-legal-links">
      <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a>
    </div>
  </div>
</footer>
'''

def cookie_banner_html(lang, lang_prefix):
    t = T[lang]
    privacy_href = lang_prefix + "legal/privacy-policy.html"
    text = t["cookie_text"].replace('Privacy &amp; Cookie Policy', f'<a href="{privacy_href}">Privacy &amp; Cookie Policy</a>') \
        if lang == "en" else t["cookie_text"].replace('Polityce prywatności i&nbsp;cookies', f'<a href="{privacy_href}">Polityce prywatności i&nbsp;cookies</a>')
    return f'''<div class="cookie-banner" data-cookie-banner role="dialog" aria-label="Cookie notice">
  <p>{text}</p>
  <div class="cookie-actions">
    <button type="button" class="btn btn-primary btn-sm" data-cookie-accept>{t['cookie_accept']}</button>
    <button type="button" class="btn btn-outline btn-sm" data-cookie-dismiss>{t['cookie_dismiss']}</button>
  </div>
</div>'''

def page(lang, lang_prefix, asset_prefix, active, title, description, canonical_path, alt_canonical_path,
         body, alt_href, og_image="assets/img/og-image.jpg", extra_scripts="", schema=""):
    h = head(lang, asset_prefix, title, description, canonical_path, alt_canonical_path, og_image)
    hdr = header_html(lang, lang_prefix, asset_prefix, active, alt_href)
    ftr = footer_html(lang, lang_prefix, asset_prefix)
    cookie = cookie_banner_html(lang, lang_prefix)
    return f'''{h}<body>
{hdr}
<main id="main">
{body}
</main>
{ftr}
{cookie}
{schema}
<script src="{asset_prefix}js/main.js" defer></script>
{extra_scripts}
</body>
</html>
'''

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

# ------------------------------------------------------------------
# Reusable icon marks for the three core services (simple line icons,
# not icon-in-a-circle clichés — flat linework matching the logo's
# geometric, angular character)
# ------------------------------------------------------------------
MARK_SUPPORT = '''<svg class="mark" viewBox="0 0 40 40" fill="none" stroke="var(--blue)" stroke-width="1.6"><rect x="6" y="9" width="28" height="18" rx="1.5"/><path d="M14 32h12M20 27v5" stroke-linecap="round"/><path d="M13 17l3 3 3-4" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
MARK_M365 = '''<svg class="mark" viewBox="0 0 40 40" fill="none" stroke="var(--blue)" stroke-width="1.6"><rect x="6" y="7" width="12" height="12" rx="1.2"/><rect x="22" y="7" width="12" height="12" rx="1.2"/><rect x="6" y="21" width="12" height="12" rx="1.2"/><rect x="22" y="21" width="12" height="12" rx="1.2"/></svg>'''
MARK_DATA = '''<svg class="mark" viewBox="0 0 40 40" fill="none" stroke="var(--blue)" stroke-width="1.6"><path d="M8 32V18M18 32V9M28 32v-9" stroke-linecap="round"/><path d="M6 32h28" stroke-linecap="round"/></svg>'''
MARK_NET = '''<svg class="mark" viewBox="0 0 40 40" fill="none" stroke="var(--blue)" stroke-width="1.6"><circle cx="20" cy="10" r="2.4"/><circle cx="9" cy="30" r="2.4"/><circle cx="31" cy="30" r="2.4"/><path d="M20 12.4V20M20 20 9 27.6M20 20l11 7.6" stroke-linecap="round"/></svg>'''
MARK_ASSETS = '''<svg class="mark" viewBox="0 0 40 40" fill="none" stroke="var(--blue)" stroke-width="1.6"><rect x="8" y="6" width="24" height="28" rx="1.5"/><path d="M13 14h14M13 20h14M13 26h9" stroke-linecap="round"/></svg>'''
MARK_DOMAIN = '''<svg class="mark" viewBox="0 0 40 40" fill="none" stroke="var(--blue)" stroke-width="1.6"><circle cx="20" cy="20" r="14"/><path d="M6 20h28M20 6c3.6 3.8 5.6 8.8 5.6 14S23.6 34.2 20 38M20 6c-3.6 3.8-5.6 8.8-5.6 14S16.4 34.2 20 38" /></svg>'''

def check_items(items):
    return "\n".join(f'<li>{ICON_CHECK}<span>{i}</span></li>' for i in items)

# ==================================================================
# Hero abstract visual (ties to the logo's rising-bars/dots motif,
# built as clean geometric SVG rather than a literal chart)
# ==================================================================
HERO_VISUAL = '''<svg viewBox="0 0 420 380" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="">
  <defs>
    <linearGradient id="barGrad" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0" stop-color="var(--navy)"/>
      <stop offset="1" stop-color="var(--blue-light)"/>
    </linearGradient>
  </defs>
  <circle cx="150" cy="150" r="108" stroke="var(--line)" stroke-width="1.5" fill="none"/>
  <path d="M150 42a108 108 0 0 1 76 184" stroke="url(#barGrad)" stroke-width="16" fill="none" stroke-linecap="round"/>
  <g>
    <rect x="120" y="230" width="34" height="90" rx="3" fill="url(#barGrad)"/>
    <rect x="164" y="205" width="34" height="115" rx="3" fill="url(#barGrad)" opacity="0.92"/>
    <rect x="208" y="175" width="34" height="145" rx="3" fill="var(--blue-light)" opacity="0.85"/>
  </g>
  <g fill="var(--blue-light)">
    <rect x="252" y="150" width="16" height="16" rx="3" opacity="0.9"/>
    <rect x="278" y="118" width="14" height="14" rx="3" opacity="0.75"/>
    <rect x="300" y="90" width="12" height="12" rx="3" opacity="0.6"/>
  </g>
</svg>'''

# ==================================================================
# About-page location graphic — abstract radiating-node cluster
# (not a literal map, avoids any geographic inaccuracy) tying the
# four service-area towns back to a central Cevano node.
# ==================================================================
ABOUT_LOCATION_GRAPHIC = '''<svg viewBox="0 0 320 300" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="">
  <defs>
    <linearGradient id="aboutGrad" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="var(--navy)"/>
      <stop offset="1" stop-color="var(--blue-light)"/>
    </linearGradient>
  </defs>
  <g stroke="var(--line)" stroke-width="1.5">
    <line x1="160" y1="150" x2="70" y2="70"/>
    <line x1="160" y1="150" x2="250" y2="60"/>
    <line x1="160" y1="150" x2="80" y2="235"/>
    <line x1="160" y1="150" x2="245" y2="225"/>
  </g>
  <circle cx="160" cy="150" r="30" fill="url(#aboutGrad)"/>
  <g fill="var(--blue-light)">
    <circle cx="70" cy="70" r="9"/>
    <circle cx="250" cy="60" r="7"/>
    <circle cx="80" cy="235" r="8"/>
    <circle cx="245" cy="225" r="6.5"/>
  </g>
  <circle cx="160" cy="150" r="30" fill="none" stroke="var(--surface)" stroke-width="3"/>
</svg>'''

print("Generator module loaded. Run build_all.py to produce pages.")
