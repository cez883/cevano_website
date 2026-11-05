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

# Wersja plików CSS/JS — dopisywana do adresu (?v=...), bo Cloudflare trzyma
# /css/* i /js/* w pamięci podręcznej 30 dni (_headers). ZMIEŃ tę wartość
# (np. na dzisiejszą datę) przy każdej zmianie css/style.css lub js/main.js.
ASSET_VERSION = "20261105-5"

# ------------------------------------------------------------------
# Icons (inline SVG, currentColor / CSS vars so they theme automatically)
# ------------------------------------------------------------------
ICON_SUN = '''<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'''
ICON_MOON = '''<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>'''
ICON_MENU = '''<svg class="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'''
ICON_CLOSE = '''<svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>'''
ICON_CHECK = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'''
# Facebook 'f' and LinkedIn 'in' marks below are traced directly from Meta's
# and LinkedIn's official logo files (outline of the real glyph, not a
# hand-drawn approximation), rendered as a flat fill so they read as a thin,
# single-colour mark consistent with the other line icons on this site.
ICON_FACEBOOK = '''<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.59 2.23 L13.76 2.0 L12.09 2.37 L10.97 2.94 L9.95 3.97 L9.26 5.42 L8.95 7.15 L8.92 9.71 L6.38 9.73 L6.38 13.5 L8.92 13.51 L8.92 21.65 L11.12 22.0 L13.4 21.93 L13.4 13.51 L16.73 13.5 L17.41 9.81 L13.41 9.73 L13.48 7.33 L13.89 6.41 L14.65 5.86 L17.62 5.66 Z"/></svg>'''
ICON_LINKEDIN = '''<svg viewBox="0 0 24 24" fill="currentColor" fill-rule="evenodd"><path d="M19.64 9.68 L20.91 12.59 L21.0 20.93 L17.25 20.93 L17.16 13.52 L16.41 12.26 L15.05 11.98 L13.97 12.35 L13.22 13.62 L13.12 20.93 L9.42 20.98 L9.38 9.02 L12.89 8.98 L12.94 10.62 L15.89 8.7 L18.19 8.88 Z M3.38 8.98 L7.03 9.02 L6.98 20.98 L3.28 20.93 Z M4.97 3.02 L5.81 3.12 L6.52 3.49 L7.03 4.05 L7.36 4.99 L7.31 5.7 L6.94 6.49 L6.33 7.05 L5.44 7.38 L4.5 7.29 L3.89 6.96 L3.23 6.21 L3.0 5.46 L3.05 4.71 L3.42 3.91 L4.03 3.35 Z"/></svg>'''

# ------------------------------------------------------------------
# Social profile links (used in the footer and in JSON-LD "sameAs")
# ------------------------------------------------------------------
SOCIAL_LINKS = [
    ("Facebook", "https://www.facebook.com/profile.php?id=61594328187021", ICON_FACEBOOK),
    ("LinkedIn", "https://www.linkedin.com/company/cevano-it-solutions/", ICON_LINKEDIN),
]

THEME_INIT_SCRIPT = '''<script>(function(){try{var t=localStorage.getItem("cevano-theme");if(t==="dark"||t==="light"){document.documentElement.setAttribute("data-theme",t);}else if(window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches){document.documentElement.setAttribute("data-theme","dark");}}catch(e){}})();</script>'''

# ------------------------------------------------------------------
# Translation strings shared across header/footer/forms
# ------------------------------------------------------------------
T = {
    "en": {
        "nav_home": "Home", "nav_services": "Services", "nav_about": "About", "nav_contact": "Contact",
        "cta_get_in_touch": "Get in touch", "cta_our_services": "Our services", "cta_email_us": "Email us",
        "skip": "Skip to main content",
        "footer_tagline": "Microsoft 365 management, websites, IT support and data analytics for small businesses across Northamptonshire and beyond.",
        "footer_company": "Company", "footer_services": "Services", "footer_legal": "Legal",
        "footer_privacy": "Privacy Policy", "footer_terms": "Terms & Conditions",
        "footer_rights": "All rights reserved.",
        "lang_name": "EN", "alt_lang_name": "PL",
        "theme_label": "Toggle dark mode",
        "menu_label": "Menu",
        "cookie_text": "Can we use analytics cookies? Google Analytics helps us see which pages are useful. It only runs if you accept, and we never use it for advertising. See our Privacy &amp; Cookie Policy for details.",
        "cookie_accept": "Accept analytics",
        "cookie_reject": "Reject",
        "cookie_settings": "Cookie settings",
    },
    "pl": {
        "nav_home": "Strona główna", "nav_services": "Usługi", "nav_about": "O nas", "nav_contact": "Kontakt",
        "cta_get_in_touch": "Skontaktuj się", "cta_our_services": "Nasze usługi", "cta_email_us": "Napisz do nas",
        "skip": "Przejdź do treści głównej",
        "footer_tagline": "Zarządzanie Microsoft 365, strony internetowe, wsparcie IT i analiza danych dla małych firm w Northamptonshire i okolicach.",
        "footer_company": "Firma", "footer_services": "Usługi", "footer_legal": "Informacje prawne",
        "footer_privacy": "Polityka prywatności", "footer_terms": "Regulamin",
        "footer_rights": "Wszelkie prawa zastrzeżone.",
        "lang_name": "PL", "alt_lang_name": "EN",
        "theme_label": "Przełącz tryb ciemny",
        "menu_label": "Menu",
        "cookie_text": "Czy możemy używać analitycznych plików cookie? Google Analytics pokazuje nam, które strony są przydatne. Działa tylko po Twojej zgodzie i nigdy nie używamy go do reklam. Szczegóły znajdziesz w naszej Polityce prywatności i&nbsp;cookies.",
        "cookie_accept": "Akceptuję analitykę",
        "cookie_reject": "Odrzucam",
        "cookie_settings": "Ustawienia cookies",
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
<link rel="stylesheet" href="{asset_prefix}css/style.css?v={ASSET_VERSION}">
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
          <a href="{home_href}" aria-current="true">{this_lang_label}</a><span aria-hidden="true">|</span><a href="{alt_href}">{other_lang_label}</a>
        </div>'''
    else:
        lang_switch = f'''<div class="lang-switch" aria-label="Language switch">
          <a href="{alt_href}">{other_lang_label}</a><span aria-hidden="true">|</span><a href="{home_href}" aria-current="true">{this_lang_label}</a>
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
    <a class="btn btn-primary btn-sm header-cta-mobile" href="{contact_href}">{t['cta_get_in_touch']}</a>
    <button type="button" class="nav-toggle" data-nav-toggle aria-label="{t['menu_label']}" aria-expanded="false">
      {ICON_MENU}{ICON_CLOSE}
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
            (services_href + "#microsoft-365", "Microsoft 365"),
            (services_href + "#websites", "Websites &amp; Landing Pages"),
            (services_href + "#it-support", "IT Support"),
            (services_href + "#data-analytics", "Data Analytics &amp; Power BI"),
        ]
    else:
        services_items = [
            (services_href + "#microsoft-365", "Microsoft 365"),
            (services_href + "#websites", "Strony internetowe"),
            (services_href + "#it-support", "Wsparcie IT"),
            (services_href + "#data-analytics", "Analiza danych i Power BI"),
        ]
    services_li = "\n".join(f'<li><a href="{h}">{lbl}</a></li>' for h, lbl in services_items)
    social_links_html = "\n        ".join(
        f'<a href="{url}" target="_blank" rel="noopener noreferrer" aria-label="{name}">{icon}</a>'
        for name, url, icon in SOCIAL_LINKS
    )
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
        Lytchett House, 13 Freeland Park<br>
        Wareham Road, Poole<br>
        Dorset, BH16 6FA
      </p>
      <div class="footer-social">
        {social_links_html}
      </div>
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
      <a href="#" data-cookie-settings>{t['cookie_settings']}</a>
    </div>
  </div>
</footer>
'''

def cookie_banner_html(lang, lang_prefix):
    t = T[lang]
    privacy_href = lang_prefix + "legal/privacy-policy.html"
    text = t["cookie_text"].replace('Privacy &amp; Cookie Policy', f'<a href="{privacy_href}">Privacy &amp; Cookie Policy</a>') \
        if lang == "en" else t["cookie_text"].replace('Polityce prywatności i&nbsp;cookies', f'<a href="{privacy_href}">Polityce prywatności i&nbsp;cookies</a>')
    return f'''<div class="cookie-banner" data-cookie-banner role="dialog" aria-label="Cookie consent">
  <p>{text}</p>
  <div class="cookie-actions">
    <button type="button" class="btn btn-primary btn-sm" data-cookie-reject>{t['cookie_reject']}</button>
    <button type="button" class="btn btn-primary btn-sm" data-cookie-accept>{t['cookie_accept']}</button>
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
<script src="{asset_prefix}js/main.js?v={ASSET_VERSION}" defer></script>
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
MARK_WEB = '''<svg class="mark" viewBox="0 0 40 40" fill="none" stroke="var(--blue)" stroke-width="1.6"><rect x="5" y="8" width="30" height="24" rx="1.5"/><path d="M5 14h30" /><path d="M10 20h12M10 25h8" stroke-linecap="round"/><rect x="26" y="19" width="5" height="8" rx="0.8"/></svg>'''

# Certificate mark: rosette with ribbon tails, same 2px stroke as other UI icons
ICON_CERT = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="9" r="6"/><path d="M8.5 13.9 7 22l5-3 5 3-1.5-8.1"/></svg>'''

def check_items(items):
    return "\n".join(f'<li>{ICON_CHECK}<span>{i}</span></li>' for i in items)

# ==================================================================
# Hero visual: a simplified Microsoft 365 user list, drawn in the site's
# hairline style. Placeholder bars stand in for names (no invented people);
# status pills show the outcome of a tidy tenant: licensed, MFA on, and a
# leaver properly offboarded. Decorative, so hidden from assistive tech.
# ==================================================================
HERO_LABELS = {
    "en": {"title": "Microsoft 365", "sub": "Users", "lic": "Licensed", "mfa": "MFA on", "off": "Offboarded"},
    "pl": {"title": "Microsoft 365", "sub": "Użytkownicy", "lic": "Licencja", "mfa": "MFA włączone", "off": "Konto wyłączone"},
}

def _pill(right, y, label, kind):
    w = round(len(label) * 6.7 + 34)
    x = right - w
    if kind == "off":
        icon = (f'<rect x="{x+12}" y="{y+10}" width="9" height="7" rx="1.2" fill="none" stroke="var(--slate)" stroke-width="1.3"/>'
                f'<path d="M{x+14} {y+10}v-2a2.5 2.5 0 0 1 5 0v2" fill="none" stroke="var(--slate)" stroke-width="1.3"/>')
        fill, color = "var(--bg)", "var(--slate)"
    else:
        icon = f'<path d="M{x+11} {y+12}l3 3 5.5-6" fill="none" stroke="var(--blue-mid)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        fill, color = "var(--bg-alt)", "var(--ink)"
    return (f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="12" fill="{fill}" stroke="var(--line)"/>{icon}'
            f'<text x="{x+26}" y="{y+16}" font-size="12" font-weight="600" fill="{color}">{label}</text>'), x

def hero_visual(lang):
    t = HERO_LABELS[lang]
    rows = []
    top, h, right = 56, 70, 398
    widths = [(118, 74), (96, 88), (132, 64), (104, 80)]
    for i, (w1, w2) in enumerate(widths):
        y = top + i * h
        cy = y + h // 2
        last = i == len(widths) - 1
        dash = ' stroke-dasharray="3 3"' if last else ""
        op = ' opacity="0.55"' if last else ""
        row = [f'<g{op}>',
               f'<circle cx="44" cy="{cy}" r="16" fill="var(--bg-alt)" stroke="var(--line)"{dash}/>',
               f'<rect x="74" y="{cy-10}" width="{w1}" height="8" rx="4" fill="var(--line)"/>',
               f'<rect x="74" y="{cy+5}" width="{w2}" height="6" rx="3" fill="var(--line)" opacity="0.6"/>',
               '</g>']
        if last:
            p, _ = _pill(right, cy - 12, t["off"], "off")
            row.append(p)
        else:
            p2, x2 = _pill(right, cy - 12, t["mfa"], "ok")
            p1, _ = _pill(x2 - 8, cy - 12, t["lic"], "ok")
            row += [p1, p2]
            row.append(f'<path d="M20 {y+h}h380" stroke="var(--line)"/>')
        rows.append("".join(row))
    body = "\n  ".join(rows)
    return (
        '<svg viewBox="0 0 420 360" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" style="font-family:var(--font-body)">\n'
        '  <rect x="1" y="1" width="418" height="358" rx="8" fill="var(--surface)" stroke="var(--line)"/>\n'
        '  <path d="M1 52h418" stroke="var(--line)"/>\n'
        '  <g fill="none" stroke="var(--blue)" stroke-width="1.4"><rect x="22" y="18" width="7" height="7" rx="0.8"/><rect x="31" y="18" width="7" height="7" rx="0.8"/><rect x="22" y="27" width="7" height="7" rx="0.8"/><rect x="31" y="27" width="7" height="7" rx="0.8"/></g>\n'
        f'  <text x="50" y="31" font-size="14" font-weight="700" fill="var(--ink)" style="font-family:var(--font-head)">{t["title"]}</text>\n'
        f'  <text x="398" y="31" font-size="12" font-weight="600" fill="var(--slate)" text-anchor="end">{t["sub"]}</text>\n'
        f'  {body}\n'
        '</svg>'
    )

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
