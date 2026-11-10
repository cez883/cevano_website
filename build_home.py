# -*- coding: utf-8 -*-
from build import *

# ================================================================
# HOMEPAGE — EN
# ================================================================
schema_home_en = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Cevano IT Solutions",
  "description": "Microsoft 365 management, websites, IT support and data analytics for small businesses in Northampton, Kettering, Milton Keynes, Rugby and surrounding areas.",
  "url": "https://www.cevano.co.uk/",
  "email": "enquiries@cevano.co.uk",
  "areaServed": ["Northampton", "Kettering", "Milton Keynes", "Rugby", "Northamptonshire", "Warwickshire", "Buckinghamshire"],
  "image": "https://www.cevano.co.uk/assets/img/og-image.jpg",
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61594328187021",
    "https://www.linkedin.com/company/cevano-it-solutions/"
  ]
}
</script>'''

body_home_en = f'''
<section class="hero hero--dark">
  {hero_bg("")}
  <div class="container hero-grid">
    <div class="hero-copy">
      <h1><span class="nw">IT.</span> <span class="nw">Web design.</span> <span class="nw">Data.</span> <span class="h1-tail">All in one place.</span></h1>
      <p class="hero-subtitle">Technology that helps your business move forward.</p>
      <p class="lede">We provide tailored IT solutions, modern websites and data analytics to help small businesses and startups work smarter, stay secure and grow with confidence.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="contact.html">Get in touch</a>
        <a class="btn btn-outline" href="services.html">Explore our services</a>
      </div>
      <ul class="hero-meta">
        <li>{I_ENVELOPE}<a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a></li>
        <li>{I_PIN}<span>On-site around Northampton, Kettering, Milton Keynes and Rugby. Remote across the UK.</span></li>
      </ul>
    </div>
    {hero_bento("en", "services.html")}
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="kicker">What we do</span>
      <h2>Four services, one point of contact</h2>
      <p>From Microsoft 365 and everyday IT support to professional websites and Power BI reporting, we bring the technology your business needs together under one roof.</p>
    </div>

    <div class="service-grid">
      <div class="service-card is-lead">
        <div class="lead-copy">
          <span class="mark-tile">{MARK_M365}</span>
          <h3>Microsoft 365</h3>
          <p>We manage your Microsoft 365 environment, from user accounts and licensing to security, permissions and device management — helping your business stay organised and secure.</p>
          <a class="btn-ghost" href="services.html#microsoft-365">Microsoft 365 in detail →</a>
        </div>
        <div class="lead-help">
          <h4 class="lead-help-title">Common ways we can help</h4>
          <ul class="check-list">
          {check_items([
              "Setting up user accounts, licences and access for new employees",
              "Managing employee access securely when someone leaves the business",
              "Organising company files, shared folders and permissions in SharePoint and OneDrive",
              "Configuring device management and security with Microsoft Intune",
          ])}
          </ul>
        </div>
      </div>
      <div class="service-card">
        <span class="mark-tile">{MARK_SUPPORT}</span>
        <h3>IT Support</h3>
        <p>Practical IT Support for the technology your business relies on every day — from troubleshooting and device setup to office moves and ongoing technical assistance.</p>
        <a class="btn-ghost" href="services.html#it-support">IT Support in detail →</a>
      </div>
      <div class="service-card">
        <span class="mark-tile">{MARK_WEB}</span>
        <h3>Web Design</h3>
        <p>Modern, professional websites and landing pages that showcase your business, communicate your services clearly and make it easy for customers to get in touch.</p>
        <a class="btn-ghost" href="services.html#websites">Web Design in detail →</a>
      </div>
      <div class="service-card">
        <span class="mark-tile">{MARK_DATA}</span>
        <h3>Data Analytics &amp; Power BI</h3>
        <p>We turn your business data into clear Power BI dashboards and reports, helping you track performance, identify trends and make better-informed decisions.</p>
        <a class="btn-ghost" href="services.html#data-analytics">Data Analytics in detail →</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Also available</span>
      <h2>Additional IT Services</h2>
      <p>Alongside our core services, we help with the practical details that keep an office running.</p>
    </div>
    <div class="subservice-grid">
      <div class="subservice-card">
        {MARK_NET}
        <h3>Networking &amp; AV</h3>
        <p>Business networking, Wi-Fi, connectivity troubleshooting and meeting room AV.</p>
      </div>
      <div class="subservice-card">
        {MARK_ASSETS}
        <h3>IT Assets &amp; Documentation</h3>
        <p>Device inventories and clear technical documentation, including support for audits.</p>
      </div>
      <div class="subservice-card">
        {MARK_DOMAIN}
        <h3>Domains &amp; Email</h3>
        <p>Domain name and DNS support, plus business email and domain setup.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="m365-problems">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Microsoft 365</span>
      <h2>Common Microsoft 365 problems we sort out</h2>
    </div>
    <div class="problem-grid">
      <div class="problem">
        <h3>Someone has left, but their account is still open</h3>
        <p>We offboard them properly: sign-in blocked, licence freed, and their mail and files secured for the team.</p>
      </div>
      <div class="problem">
        <h3>An important email never arrived</h3>
        <p>We trace the message, find out where it went, and release it from quarantine if it was blocked by mistake.</p>
      </div>
      <div class="problem">
        <h3>A file was deleted or overwritten</h3>
        <p>We recover it from the OneDrive or SharePoint recycle bin, or restore an earlier version.</p>
      </div>
      <div class="problem">
        <h3>A laptop or phone has gone missing</h3>
        <p>If it's enrolled in Intune, we wipe company data from it remotely. We can also enforce encryption and a PIN so the next one is protected.</p>
      </div>
    </div>
    <div class="review-offer">
      <div>
        <h3>Not sure what state your Microsoft 365 is in?</h3>
        <p>We'll review your setup for free and tell you what we'd fix first.</p>
      </div>
      <a class="btn btn-outline" href="contact.html?service=m365">Ask for a free review</a>
    </div>
  </div>
</section>

<section class="section section-alt" id="how-it-works">
  <div class="container">
    <div class="section-head">
      <span class="kicker">How it works</span>
      <h2>Getting started is straightforward</h2>
    </div>
    <div class="process-grid">
      <div class="process-step">
        <span class="step-num">1</span>
        <h3>Tell us what's going on</h3>
        <p>Send a message or email describing the problem or project — no need to know the technical details first.</p>
      </div>
      <div class="process-step">
        <span class="step-num">2</span>
        <h3>We work out the right approach</h3>
        <p>We'll ask a few questions, explain the options in plain terms, and agree a practical way forward.</p>
      </div>
      <div class="process-step">
        <span class="step-num">3</span>
        <h3>We get it sorted</h3>
        <p>Whether it's a quick fix or ongoing support, we handle it — and keep you in the loop as we go.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Not sure where to start?</h2>
        <p>Describe what's not working in a few lines. We'll reply by email with the options.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Get in touch</a>
    </div>
  </div>
</section>
'''

write("index.html", page(
    "en", "", "", "home",
    "Microsoft 365, IT Support &amp; Websites for Small Businesses | Cevano",
    "Microsoft 365 management, websites, IT support and data analytics for small businesses in Northampton, Kettering, Milton Keynes, Rugby and surrounding areas.",
    "", "", body_home_en, alt_href="pl/index.html", schema=schema_home_en
))

# ================================================================
# HOMEPAGE — PL
# ================================================================
schema_home_pl = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Cevano IT Solutions",
  "description": "Zarządzanie Microsoft 365, strony internetowe, wsparcie IT i analiza danych dla małych firm w Northampton, Kettering, Milton Keynes, Rugby i okolicach.",
  "url": "https://www.cevano.co.uk/pl/",
  "email": "enquiries@cevano.co.uk",
  "areaServed": ["Northampton", "Kettering", "Milton Keynes", "Rugby", "Northamptonshire", "Warwickshire", "Buckinghamshire"],
  "image": "https://www.cevano.co.uk/assets/img/og-image.jpg",
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61594328187021",
    "https://www.linkedin.com/company/cevano-it-solutions/"
  ]
}
</script>'''

body_home_pl = f'''
<section class="hero hero--dark">
  {hero_bg("../")}
  <div class="container hero-grid">
    <div class="hero-copy">
      <h1><span class="nw">IT Support.</span> <span class="nw">Strony WWW.</span> <span class="nw">Analiza danych.</span> <span class="h1-tail">Wszystko w jednym miejscu.</span></h1>
      <p class="hero-subtitle">Technologia, która pomaga Twojej firmie iść do przodu.</p>
      <p class="lede">Pomagamy małym firmom i startupom działać sprawniej i bezpieczniej dzięki rozwiązaniom IT, nowoczesnym stronom internetowym i analizie danych.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="contact.html">Skontaktuj się</a>
        <a class="btn btn-outline" href="services.html">Poznaj nasze usługi</a>
      </div>
      <ul class="hero-meta">
        <li>{I_ENVELOPE}<a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a></li>
        <li>{I_PIN}<span>Działamy lokalnie w okolicach Northampton, Kettering, Milton Keynes i Rugby, a zdalnie na terenie całej Wielkiej Brytanii.</span></li>
      </ul>
    </div>
    {hero_bento("pl", "services.html")}
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Co robimy?</span>
      <h2>Cztery obszary usług, jeden partner.</h2>
      <p>Od Microsoft 365 i codziennego wsparcia IT po profesjonalne strony internetowe i raportowanie Power BI — zapewniamy technologie, których potrzebuje Twoja firma, w jednym miejscu.</p>
    </div>

    <div class="service-grid">
      <div class="service-card is-lead">
        <div class="lead-copy">
          <span class="mark-tile">{MARK_M365}</span>
          <h3>Microsoft 365</h3>
          <p>Zajmujemy się obsługą środowiska Microsoft 365 — od kont użytkowników i licencji po bezpieczeństwo, uprawnienia i zarządzanie urządzeniami. Pomagamy Twojej firmie działać sprawnie i bezpiecznie.</p>
          <a class="btn-ghost" href="services.html#microsoft-365">Więcej o Microsoft 365 →</a>
        </div>
        <div class="lead-help">
          <h4 class="lead-help-title">Jak możemy pomóc?</h4>
          <ul class="check-list">
          {check_items([
              "Konfiguracja kont użytkowników, licencji i dostępów dla nowych pracowników",
              "Bezpieczne odbieranie dostępów pracownikom kończącym współpracę z firmą",
              "Porządkowanie firmowych plików, folderów współdzielonych i uprawnień w SharePoint i OneDrive",
              "Konfiguracja zarządzania urządzeniami i zabezpieczeń za pomocą Microsoft Intune",
          ])}
          </ul>
        </div>
      </div>
      <div class="service-card">
        <span class="mark-tile">{MARK_SUPPORT}</span>
        <h3>IT Support</h3>
        <p>Praktyczne wsparcie IT w codziennych potrzebach Twojej firmy — od rozwiązywania problemów i konfiguracji urządzeń po przeprowadzki biur i bieżącą pomoc techniczną.</p>
        <a class="btn-ghost" href="services.html#it-support">Więcej o IT Support →</a>
      </div>
      <div class="service-card">
        <span class="mark-tile">{MARK_WEB}</span>
        <h3>Web Design</h3>
        <p>Nowoczesne, profesjonalne strony internetowe i landing page, które prezentują Twoją firmę, jasno przedstawiają ofertę i ułatwiają klientom kontakt.</p>
        <a class="btn-ghost" href="services.html#websites">Więcej o Web Design →</a>
      </div>
      <div class="service-card">
        <span class="mark-tile">{MARK_DATA}</span>
        <h3>Data Analytics &amp; Power BI</h3>
        <p>Przekształcamy dane Twojej firmy w przejrzyste dashboardy i raporty Power BI, które pomagają monitorować wyniki, dostrzegać trendy i podejmować lepsze decyzje biznesowe.</p>
        <a class="btn-ghost" href="services.html#data-analytics">Więcej o Data Analytics →</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Dostępne również</span>
      <h2>Dodatkowe Usługi IT</h2>
      <p>Oprócz naszych głównych usług pomagamy również w praktycznych sprawach, które utrzymują biuro w sprawnym działaniu.</p>
    </div>
    <div class="subservice-grid">
      <div class="subservice-card">
        {MARK_NET}
        <h3>Sieci i AV</h3>
        <p>Sieci firmowe, Wi-Fi, rozwiązywanie problemów z łącznością oraz sprzęt AV w salach spotkań.</p>
      </div>
      <div class="subservice-card">
        {MARK_ASSETS}
        <h3>Zasoby IT i dokumentacja</h3>
        <p>Inwentaryzacja urządzeń oraz przejrzysta dokumentacja techniczna, w tym wsparcie przy audytach.</p>
      </div>
      <div class="subservice-card">
        {MARK_DOMAIN}
        <h3>Domeny i poczta</h3>
        <p>Wsparcie w zakresie domen i DNS oraz konfiguracja poczty firmowej i domeny.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="m365-problems">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Microsoft 365</span>
      <h2>Typowe problemy z Microsoft 365, które rozwiązujemy</h2>
    </div>
    <div class="problem-grid">
      <div class="problem">
        <h3>Ktoś odszedł, a jego konto wciąż działa</h3>
        <p>Prawidłowo zamykamy dostęp: blokujemy logowanie, zwalniamy licencję i zabezpieczamy pocztę oraz pliki dla zespołu.</p>
      </div>
      <div class="problem">
        <h3>Ważny e-mail nie dotarł</h3>
        <p>Śledzimy wiadomość, sprawdzamy, gdzie trafiła, i uwalniamy ją z kwarantanny, jeśli została zablokowana przez pomyłkę.</p>
      </div>
      <div class="problem">
        <h3>Plik został usunięty lub nadpisany</h3>
        <p>Odzyskujemy go z kosza OneDrive lub SharePoint albo przywracamy wcześniejszą wersję.</p>
      </div>
      <div class="problem">
        <h3>Zginął laptop lub telefon</h3>
        <p>Jeśli urządzenie jest w Intune, zdalnie usuwamy z niego firmowe dane. Możemy też wymusić szyfrowanie i kod PIN, żeby kolejne było chronione.</p>
      </div>
    </div>
    <div class="review-offer">
      <div>
        <h3>Nie wiesz, w jakim stanie jest Twój Microsoft 365?</h3>
        <p>Bezpłatnie przejrzymy Twoją konfigurację i powiemy, co naprawilibyśmy w pierwszej kolejności.</p>
      </div>
      <a class="btn btn-outline" href="contact.html?service=m365">Poproś o bezpłatny przegląd</a>
    </div>
  </div>
</section>

<section class="section section-alt" id="how-it-works">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Jak przebiega współpraca</span>
      <h2>Rozpoczęcie współpracy jest proste</h2>
    </div>
    <div class="process-grid">
      <div class="process-step">
        <span class="step-num">1</span>
        <h3>Opisz, z czym się mierzysz</h3>
        <p>Napisz wiadomość lub e-mail z opisem problemu lub projektu — nie musisz znać szczegółów technicznych.</p>
      </div>
      <div class="process-step">
        <span class="step-num">2</span>
        <h3>Wspólnie ustalamy podejście</h3>
        <p>Zadamy kilka pytań, wyjaśnimy dostępne opcje prostym językiem i uzgodnimy praktyczny sposób działania.</p>
      </div>
      <div class="process-step">
        <span class="step-num">3</span>
        <h3>Zajmujemy się realizacją</h3>
        <p>Niezależnie czy to szybka naprawa, czy stałe wsparcie — zajmiemy się tym i będziemy Cię informować na bieżąco.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Nie wiesz, od czego zacząć?</h2>
        <p>Opisz w kilku zdaniach, co nie działa. Odpowiemy e-mailem i przedstawimy możliwości.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Skontaktuj się</a>
    </div>
  </div>
</section>
'''

write("pl/index.html", page(
    "pl", "", "../", "home",
    "Microsoft 365, wsparcie IT i strony internetowe dla małych firm | Cevano",
    "Zarządzanie Microsoft 365, strony internetowe, wsparcie IT i analiza danych dla małych firm w Northampton, Kettering, Milton Keynes, Rugby i okolicach.",
    "", "", body_home_pl, alt_href="../index.html", schema=schema_home_pl
))
