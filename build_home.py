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
  "description": "Practical IT support, Microsoft 365 management and data analytics for small businesses in Northampton, Kettering, Milton Keynes, Rugby and surrounding areas.",
  "url": "https://www.cevano.co.uk/",
  "email": "enquiries@cevano.co.uk",
  "areaServed": ["Northampton", "Kettering", "Milton Keynes", "Rugby", "Northamptonshire", "Warwickshire", "Buckinghamshire"],
  "image": "https://www.cevano.co.uk/assets/img/og-image.jpg",
  "sameAs": []
}
</script>'''

body_home_en = f'''
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">IT support across Northamptonshire &amp; beyond</span>
      <h1>Technology should make your business easier, not harder.</h1>
      <p class="lede">Cevano IT Solutions provides practical IT support, Microsoft 365 management and data analytics for small businesses, sole traders and startups — around Northampton, Kettering, Milton Keynes and Rugby, with remote support wherever you're based.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="contact.html">Get in touch</a>
        <a class="btn btn-outline" href="services.html">Our services</a>
      </div>
      <p class="hero-email">Prefer email? Write to <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a></p>
      <p class="trust-badge">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12Z"/><circle cx="12" cy="9" r="2.5"/></svg>
        Supporting small businesses across Northamptonshire
      </p>
    </div>
    <div class="hero-visual">{HERO_VISUAL}</div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="kicker">What we do</span>
      <h2>Three services, one trusted provider</h2>
      <p>Everyday IT support, a properly managed Microsoft 365 environment, and data you can actually use — without juggling three different suppliers.</p>
    </div>

    <div class="flow-row" aria-hidden="true">
      <span>IT Support</span><span class="line"></span><span class="dot"></span><span class="line"></span>
      <span>Microsoft 365</span><span class="line"></span><span class="dot"></span><span class="line"></span>
      <span>Data Analytics</span>
    </div>

    <div class="service-grid">
      <div class="service-card">
        {MARK_SUPPORT}
        <h3>IT Support</h3>
        <p>Practical technology support for small businesses, offices and professionals — from everyday troubleshooting to setting up a new office.</p>
        <a class="btn-ghost" href="services.html#it-support">Learn more →</a>
      </div>
      <div class="service-card">
        {MARK_M365}
        <h3>Microsoft 365</h3>
        <p>Microsoft 365 administration covering user accounts, licensing, security, permissions and device management.</p>
        <a class="btn-ghost" href="services.html#microsoft-365">Learn more →</a>
      </div>
      <div class="service-card">
        {MARK_DATA}
        <h3>Data Analytics &amp; Power BI</h3>
        <p>Turning business data into clear Power BI dashboards, reports and insight you can act on.</p>
        <a class="btn-ghost" href="services.html#data-analytics">Learn more →</a>
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
        <h3>Domains &amp; Online Services</h3>
        <p>Domain name and DNS support, business email/domain setup, and web or landing page design.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="why-cevano">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Why Cevano</span>
      <h2>Built around small businesses, not enterprise IT departments</h2>
    </div>
    <div class="why-grid">
      <div class="why-card">
        <h3>One point of contact</h3>
        <p>IT support, Microsoft 365 and data analytics from one trusted provider, instead of three different suppliers.</p>
      </div>
      <div class="why-card">
        <h3>Practical approach</h3>
        <p>Clear explanations and clear solutions, without unnecessary technical complexity.</p>
      </div>
      <div class="why-card">
        <h3>Flexible support</h3>
        <p>Designed around the needs of small businesses and sole traders, not enterprise-sized organisations.</p>
      </div>
      <div class="why-card">
        <h3>Business-focused</h3>
        <p>Technology should support the business, not become another problem to manage.</p>
      </div>
      <div class="why-card">
        <h3>Local &amp; remote support</h3>
        <p>Supporting businesses around Northampton, Kettering, Milton Keynes, Rugby and the surrounding areas, with remote support where it makes sense.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="how-it-works">
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

<section class="section section-alt" id="about-preview">
  <div class="container about-layout">
    <div>
      <span class="kicker">About Cevano</span>
      <h2>An approachable technology partner for small businesses</h2>
      <p>Cevano IT Solutions provides practical technology support for individuals, sole traders, startups and small businesses. We bring IT support, Microsoft 365 and data analytics together under one roof, so you have one place to go for the technology decisions that affect your business.</p>
      <a class="btn-ghost" href="about.html">More about Cevano →</a>
    </div>
    <ul class="about-list">
      <li>Approachable expertise, explained in plain terms</li>
      <li>Practical solutions over unnecessary complexity</li>
      <li>Flexible support built around your business</li>
      <li>IT, Microsoft 365 and data analytics under one roof</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Ready to make technology easier for your business?</h2>
        <p>Tell us what you need help with and we'll get back to you.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Get in touch</a>
    </div>
  </div>
</section>
'''

write("index.html", page(
    "en", "", "", "home",
    "Cevano IT Solutions | IT Support, Microsoft 365 &amp; Data Analytics",
    "Practical IT support, Microsoft 365 management and data analytics for small businesses in Northampton, Kettering, Milton Keynes, Rugby and surrounding areas.",
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
  "description": "Praktyczne wsparcie IT, zarządzanie Microsoft 365 i analiza danych dla małych firm w Northampton, Kettering, Milton Keynes, Rugby i okolicach.",
  "url": "https://www.cevano.co.uk/pl/",
  "email": "enquiries@cevano.co.uk",
  "areaServed": ["Northampton", "Kettering", "Milton Keynes", "Rugby", "Northamptonshire", "Warwickshire", "Buckinghamshire"],
  "image": "https://www.cevano.co.uk/assets/img/og-image.jpg",
  "sameAs": []
}
</script>'''

body_home_pl = f'''
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">Wsparcie IT w Northamptonshire i okolicach</span>
      <h1>Technologia ma ułatwiać prowadzenie firmy, a nie je utrudniać.</h1>
      <p class="lede">Cevano IT Solutions zapewnia praktyczne wsparcie IT, zarządzanie Microsoft 365 oraz analizę danych dla małych firm, jednoosobowych działalności i startupów — w okolicach Northampton, Kettering, Milton Keynes i Rugby, a zdalnie tam, gdzie akurat jesteś.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="contact.html">Skontaktuj się</a>
        <a class="btn btn-outline" href="services.html">Nasze usługi</a>
      </div>
      <p class="hero-email">Wolisz e-mail? Napisz na <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a></p>
      <p class="trust-badge">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12Z"/><circle cx="12" cy="9" r="2.5"/></svg>
        Wspieramy małe firmy w całym Northamptonshire
      </p>
    </div>
    <div class="hero-visual">{HERO_VISUAL}</div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Czym się zajmujemy</span>
      <h2>Trzy usługi, jeden zaufany dostawca</h2>
      <p>Codzienne wsparcie IT, dobrze zarządzane środowisko Microsoft 365 i dane, z których faktycznie da się korzystać — bez konieczności współpracy z trzema różnymi dostawcami.</p>
    </div>

    <div class="flow-row" aria-hidden="true">
      <span>Wsparcie IT</span><span class="line"></span><span class="dot"></span><span class="line"></span>
      <span>Microsoft 365</span><span class="line"></span><span class="dot"></span><span class="line"></span>
      <span>Analiza danych</span>
    </div>

    <div class="service-grid">
      <div class="service-card">
        {MARK_SUPPORT}
        <h3>Wsparcie IT</h3>
        <p>Praktyczne wsparcie technologiczne dla małych firm, biur i specjalistów — od codziennych problemów po organizację nowego biura.</p>
        <a class="btn-ghost" href="services.html#it-support">Dowiedz się więcej →</a>
      </div>
      <div class="service-card">
        {MARK_M365}
        <h3>Microsoft 365</h3>
        <p>Administracja Microsoft 365 obejmująca konta użytkowników, licencje, bezpieczeństwo, uprawnienia i zarządzanie urządzeniami.</p>
        <a class="btn-ghost" href="services.html#microsoft-365">Dowiedz się więcej →</a>
      </div>
      <div class="service-card">
        {MARK_DATA}
        <h3>Analiza danych i Power BI</h3>
        <p>Przekształcanie danych biznesowych w przejrzyste pulpity Power BI, raporty i wnioski, na których można polegać.</p>
        <a class="btn-ghost" href="services.html#data-analytics">Dowiedz się więcej →</a>
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
        <h3>Domeny i usługi online</h3>
        <p>Wsparcie w zakresie domen i DNS, konfiguracja poczty firmowej i domeny oraz projektowanie stron i landing page'y.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="why-cevano">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Dlaczego Cevano</span>
      <h2>Stworzone z myślą o małych firmach, nie o działach IT dużych korporacji</h2>
    </div>
    <div class="why-grid">
      <div class="why-card">
        <h3>Jeden punkt kontaktu</h3>
        <p>Wsparcie IT, Microsoft 365 i analiza danych od jednego zaufanego dostawcy zamiast trzech różnych firm.</p>
      </div>
      <div class="why-card">
        <h3>Praktyczne podejście</h3>
        <p>Jasne wyjaśnienia i jasne rozwiązania, bez zbędnej technicznej złożoności.</p>
      </div>
      <div class="why-card">
        <h3>Elastyczne wsparcie</h3>
        <p>Dopasowane do potrzeb małych firm i jednoosobowych działalności, a nie organizacji wielkości korporacji.</p>
      </div>
      <div class="why-card">
        <h3>Nastawienie na biznes</h3>
        <p>Technologia ma wspierać firmę, a nie stawać się kolejnym problemem do zarządzania.</p>
      </div>
      <div class="why-card">
        <h3>Wsparcie lokalne i zdalne</h3>
        <p>Wspieramy firmy w okolicach Northampton, Kettering, Milton Keynes, Rugby i w sąsiednich obszarach, oferując wsparcie zdalne tam, gdzie ma to sens.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="how-it-works">
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

<section class="section section-alt" id="about-preview">
  <div class="container about-layout">
    <div>
      <span class="kicker">O Cevano</span>
      <h2>Przystępny partner technologiczny dla małych firm</h2>
      <p>Cevano IT Solutions zapewnia praktyczne wsparcie technologiczne dla osób prywatnych, jednoosobowych działalności, startupów i małych firm. Łączymy wsparcie IT, Microsoft 365 i analizę danych w jednym miejscu, dzięki czemu masz jeden adres, do którego zwracasz się w sprawach technologicznych dotyczących Twojej firmy.</p>
      <a class="btn-ghost" href="about.html">Więcej o Cevano →</a>
    </div>
    <ul class="about-list">
      <li>Przystępna wiedza ekspercka, wyjaśniana prostym językiem</li>
      <li>Praktyczne rozwiązania zamiast zbędnej złożoności</li>
      <li>Elastyczne wsparcie dopasowane do Twojej firmy</li>
      <li>IT, Microsoft 365 i analiza danych w jednym miejscu</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Gotowy, aby technologia stała się prostsza dla Twojej firmy?</h2>
        <p>Napisz, z czym potrzebujesz pomocy, a odezwiemy się do Ciebie.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Skontaktuj się</a>
    </div>
  </div>
</section>
'''

write("pl/index.html", page(
    "pl", "", "../", "home",
    "Cevano IT Solutions | Wsparcie IT, Microsoft 365 i analiza danych",
    "Praktyczne wsparcie IT, zarządzanie Microsoft 365 i analiza danych dla małych firm w Northampton, Kettering, Milton Keynes, Rugby i okolicach.",
    "", "", body_home_pl, alt_href="../index.html", schema=schema_home_pl
))
