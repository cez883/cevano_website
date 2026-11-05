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
<section class="hero">
  <div class="container hero-grid">
    <div>
      <h1>Microsoft 365, set up properly and kept that way.</h1>
      <p class="lede">We manage Microsoft 365 for small businesses (accounts, licences, security and devices) and take care of the IT support and websites around it.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="contact.html">Get in touch</a>
        <a class="btn btn-outline" href="services.html">See our services</a>
      </div>
      <p class="hero-email">Prefer email? Write to <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a></p>
      <p class="trust-badge">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12Z"/><circle cx="12" cy="9" r="2.5"/></svg>
        On-site around Northampton, Kettering, Milton Keynes and Rugby. Remote across the UK.
      </p>
    </div>
    <div class="hero-visual">{hero_visual('en')}</div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="kicker">What we do</span>
      <h2>Four services, one point of contact</h2>
      <p>A properly managed Microsoft 365 environment, a website that explains what you do, everyday IT support and data you can actually use, without juggling different suppliers.</p>
    </div>

    <div class="service-grid">
      <div class="service-card is-lead">
        <div class="lead-copy">
          {MARK_M365}
          <h3>Microsoft 365</h3>
          <p>Microsoft 365 managed for you: user accounts, licensing, security, permissions and devices, without employing a full-time administrator.</p>
          <a class="btn-ghost" href="services.html#microsoft-365">Microsoft 365 in detail →</a>
        </div>
        <ul class="check-list">
          {check_items([
              "A new employee has the right access from day one",
              "Leavers are offboarded properly, with nothing left open",
              "Company files are organised and easy to find in SharePoint",
              "Licensing matches what your team actually needs",
          ])}
        </ul>
      </div>
      <div class="service-card">
        {MARK_WEB}
        <h3>Websites &amp; Landing Pages</h3>
        <p>Websites and landing pages for small businesses that explain clearly what you do, with the domain, DNS and business email set up behind them.</p>
        <a class="btn-ghost" href="services.html#websites">Websites in detail →</a>
      </div>
      <div class="service-card">
        {MARK_SUPPORT}
        <h3>IT Support</h3>
        <p>Practical technology support for small businesses, offices and professionals — from everyday troubleshooting to setting up a new office.</p>
        <a class="btn-ghost" href="services.html#it-support">IT support in detail →</a>
      </div>
      <div class="service-card">
        {MARK_DATA}
        <h3>Data Analytics &amp; Power BI</h3>
        <p>Turning business data into clear Power BI dashboards, reports and insight you can act on.</p>
        <a class="btn-ghost" href="services.html#data-analytics">Data analytics in detail →</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Also available</span>
      <h2>Additional support when you need it</h2>
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
<section class="hero">
  <div class="container hero-grid">
    <div>
      <h1>Microsoft 365 skonfigurowany porządnie i tak utrzymany.</h1>
      <p class="lede">Zarządzamy Microsoft 365 w małych firmach (konta, licencje, bezpieczeństwo i urządzenia) i zajmujemy się wsparciem IT oraz stronami internetowymi wokół niego.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="contact.html">Skontaktuj się</a>
        <a class="btn btn-outline" href="services.html">Zobacz usługi</a>
      </div>
      <p class="hero-email">Wolisz e-mail? Napisz na <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a></p>
      <p class="trust-badge">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12Z"/><circle cx="12" cy="9" r="2.5"/></svg>
        Na miejscu w okolicach Northampton, Kettering, Milton Keynes i Rugby. Zdalnie w całej Wielkiej Brytanii.
      </p>
    </div>
    <div class="hero-visual">{hero_visual('pl')}</div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Czym się zajmujemy</span>
      <h2>Cztery usługi, jeden punkt kontaktu</h2>
      <p>Dobrze zarządzane środowisko Microsoft 365, strona internetowa, która jasno mówi, czym się zajmujesz, codzienne wsparcie IT i dane, z których da się korzystać, bez żonglowania dostawcami.</p>
    </div>

    <div class="service-grid">
      <div class="service-card is-lead">
        <div class="lead-copy">
          {MARK_M365}
          <h3>Microsoft 365</h3>
          <p>Zarządzamy Twoim Microsoft 365: konta użytkowników, licencje, bezpieczeństwo, uprawnienia i urządzenia, bez zatrudniania administratora na pełen etat.</p>
          <a class="btn-ghost" href="services.html#microsoft-365">Microsoft 365 szczegółowo →</a>
        </div>
        <ul class="check-list">
          {check_items([
              "Nowy pracownik ma odpowiedni dostęp od pierwszego dnia",
              "Konta osób odchodzących są prawidłowo zamykane",
              "Firmowe pliki są uporządkowane i łatwe do znalezienia w SharePoint",
              "Licencje odpowiadają rzeczywistym potrzebom zespołu",
          ])}
        </ul>
      </div>
      <div class="service-card">
        {MARK_WEB}
        <h3>Strony internetowe</h3>
        <p>Strony i landing page dla małych firm, które jasno mówią, czym się zajmujesz, wraz z domeną, DNS i firmową pocztą.</p>
        <a class="btn-ghost" href="services.html#websites">Strony internetowe szczegółowo →</a>
      </div>
      <div class="service-card">
        {MARK_SUPPORT}
        <h3>Wsparcie IT</h3>
        <p>Praktyczne wsparcie technologiczne dla małych firm, biur i specjalistów — od codziennych problemów po organizację nowego biura.</p>
        <a class="btn-ghost" href="services.html#it-support">Wsparcie IT szczegółowo →</a>
      </div>
      <div class="service-card">
        {MARK_DATA}
        <h3>Analiza danych i Power BI</h3>
        <p>Przekształcanie danych biznesowych w przejrzyste pulpity Power BI, raporty i wnioski, na których można polegać.</p>
        <a class="btn-ghost" href="services.html#data-analytics">Analiza danych szczegółowo →</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Dostępne również</span>
      <h2>Dodatkowe wsparcie, gdy go potrzebujesz</h2>
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
