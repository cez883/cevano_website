# -*- coding: utf-8 -*-
from build import *

# ================================================================
# SERVICES — EN
# ================================================================
body_services_en = f'''
<section class="page-hero">
  <div class="container">
    <h1>Everything your business needs to work smarter</h1>
    <p>From Microsoft 365 and everyday IT support to modern websites and Power BI reporting, we provide practical technology solutions for small businesses and startups.</p>
  </div>
</section>

<nav class="mini-nav" data-mini-nav aria-label="Services on this page">
  <div class="mini-nav-inner">
    <a href="#microsoft-365">Microsoft 365</a>
    <a href="#websites">Web Design</a>
    <a href="#it-support">IT Support</a>
    <a href="#data-analytics">Data Analytics</a>
    <a href="#additional-services">Additional Services</a>
  </div>
</nav>

<section class="detail-service section-alt" id="microsoft-365">
  <div class="container detail-grid">
    <div class="detail-copy">
      {MARK_M365}
      <h2 style="margin-top:14px;">Microsoft 365, managed properly.</h2>
      <p>From user accounts and licensing to security, permissions and device management, Cevano helps small businesses get more from Microsoft 365 while keeping their environment organised and secure — without needing to employ a full-time administrator.</p>
      <ul class="check-list">
        {check_items([
            "User accounts, onboarding and offboarding",
            "Microsoft 365 licensing",
            "Security groups and permissions management",
            "Microsoft 365 security configuration",
            "Device configuration and Microsoft Intune",
            "SharePoint, OneDrive and Microsoft Teams support",
            "Microsoft 365 migrations where appropriate",
        ])}
      </ul>
      <a class="btn btn-outline service-ask" href="contact.html?service=m365">Ask about Microsoft 365</a>
    </div>
    <div class="panel">
      <h3>What this looks like in practice</h3>
      <ul>
        <li>A new employee has the right access from day one</li>
        <li>Leavers are offboarded properly, with nothing left open</li>
        <li>Company files are organised and easy to find in SharePoint</li>
        <li>Devices are set up consistently with Intune</li>
        <li>Licensing matches what your team actually needs</li>
      </ul>
    </div>
  </div>
</section>

<section class="detail-service" id="websites">
  <div class="container detail-grid reverse">
    <div class="detail-copy">
      {MARK_WEB}
      <h2 style="margin-top:14px;">Websites that make your business look professional.</h2>
      <p>Modern, responsive websites and landing pages designed to clearly communicate what you do and make it easy for customers to get in touch. We handle everything from the website itself to hosting, domain and business email setup.</p>
      <ul class="check-list">
        {check_items([
            "Single-page landing pages",
            "Small business websites",
            "Responsive design for phones, tablets and desktops",
            "Contact forms that send enquiries straight to your inbox",
            "Hosting and website setup",
            "Domain, DNS and business email configuration",
        ])}
      </ul>
      <a class="btn btn-outline service-ask" href="contact.html?service=website">Ask about a website</a>
    </div>
    <div class="panel">
      <h3>Websites built around your business</h3>
      <ul>
        <li>A professional website that clearly explains your services</li>
        <li>A focused landing page for a new service, product or campaign</li>
        <li>A simple way for potential customers to get in touch</li>
        <li>A complete setup covering your domain, hosting and business email</li>
      </ul>
    </div>
  </div>
</section>

<section class="detail-service section-alt" id="it-support">
  <div class="container detail-grid">
    <div>{MARK_SUPPORT}
      <h2 style="margin-top:14px;">IT Support that keeps your business running.</h2>
      <p>Reliable, practical IT Support for the technology your business depends on every day. From troubleshooting and device setup to office moves and technical advice, we help keep your systems working and your people productive.</p>
      <ul class="check-list">
        {check_items([
            "General IT Support and troubleshooting",
            "Hardware and software support",
            "PC and laptop setup and configuration",
            "On-site and remote IT Support",
            "Office moves and technical relocation setup",
            "Practical IT advice and consultancy",
        ])}
      </ul>
      <a class="btn btn-outline service-ask" href="contact.html?service=it-support">Ask about IT support</a>
    </div>
    <div class="panel">
      <h3>Common ways we can help</h3>
      <ul>
        <li>Setting up new users, PCs, laptops and Microsoft 365 accounts</li>
        <li>Troubleshooting Microsoft 365, email, printers, Wi-Fi and network issues</li>
        <li>Fixing recurring IT problems and identifying the root cause</li>
        <li>Setting up and supporting IT for new or relocated offices</li>
        <li>Providing practical advice on hardware, software and IT improvements</li>
      </ul>
    </div>
  </div>
</section>

<section class="detail-service" id="data-analytics">
  <div class="container detail-grid reverse">
    <div class="detail-copy">
      {MARK_DATA}
      <h2 style="margin-top:14px;">Turn your data into better business decisions.</h2>
      <p>We help small businesses turn data from Excel, business systems and other sources into clear, useful Power BI dashboards and reports. We make your data easier to understand, helping you track performance, spot trends and make more informed decisions.</p>
      <p class="trust-badge">{ICON_CERT}Microsoft Certified: Power BI Data Analyst Associate (PL-300)</p>
      <ul class="check-list">
        {check_items([
            "Data analysis and business intelligence",
            "Power BI dashboards and data visualisation",
            "KPI and performance reporting",
            "Data transformation and preparation with Power Query",
            "Turning spreadsheets and business data into useful insights",
            "Reports designed for management meetings and business reviews",
        ])}
      </ul>
      <a class="btn btn-outline service-ask" href="contact.html?service=data">Ask about Power BI</a>
    </div>
    <div class="panel">
      <h3>Common ways we can help</h3>
      <ul>
        <li>Bringing sales, financial or operational data into one clear dashboard</li>
        <li>Replacing manual Excel reports with automated Power BI reporting</li>
        <li>Tracking the KPIs that matter most to your business</li>
        <li>Combining data from multiple sources into a single view</li>
        <li>Creating clear reports for management meetings and business reviews</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-alt" id="additional-services">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Additional IT Services</span>
      <h2>The extra services that keep your business connected and organised.</h2>
      <p>Alongside our core services, we provide additional technical support to help small businesses manage their office technology, IT equipment, network infrastructure and online services.</p>
    </div>
    <div class="subservice-grid">
      <div class="subservice-card">
        {MARK_NET}
        <h3>Networking &amp; AV</h3>
        <p>Reliable connectivity and meeting room technology for your workplace.</p>
        <ul>
          <li>Business network and Wi-Fi setup</li>
          <li>Network troubleshooting and connectivity support</li>
          <li>Office network infrastructure</li>
          <li>Meeting room AV and video conferencing systems</li>
          <li>Network cabling and communications cabinet support</li>
        </ul>
      </div>
      <div class="subservice-card">
        {MARK_ASSETS}
        <h3>IT Assets &amp; Documentation</h3>
        <p>A clear picture of your IT equipment, systems and technical setup.</p>
        <ul>
          <li>IT asset and device inventories</li>
          <li>Hardware and software records</li>
          <li>IT infrastructure and system documentation</li>
          <li>Technical documentation for audits and reviews</li>
          <li>Asset tracking and lifecycle records</li>
        </ul>
      </div>
      <div class="subservice-card">
        {MARK_DOMAIN}
        <h3>Domains &amp; Email</h3>
        <p>The essential services behind your website and business communications.</p>
        <ul>
          <li>Domain registration and configuration</li>
          <li>DNS management and troubleshooting</li>
          <li>Business email setup and configuration</li>
          <li>Domain and email integration with Microsoft 365</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Not sure which service is right for your business?</h2>
        <p>Tell us what you need help with, and we'll find the right solution for you.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Get in touch</a>
    </div>
  </div>
</section>
'''

write("services.html", page(
    "en", "", "", "services",
    "Services | Microsoft 365, Websites, IT Support &amp; Data Analytics — Cevano",
    "Microsoft 365 administration, websites and landing pages, IT support and Power BI data analytics for small businesses, explained in plain English.",
    "services.html", "services.html", body_services_en, alt_href="pl/services.html"
))

# ================================================================
# SERVICES — PL
# ================================================================
body_services_pl = f'''
<section class="page-hero">
  <div class="container">
    <h1>Wszystko, czego Twoja firma potrzebuje, by pracować mądrzej</h1>
    <p>Od Microsoft 365 i codziennego wsparcia IT po nowoczesne strony internetowe i raporty Power BI – dostarczamy praktyczne rozwiązania technologiczne dla małych firm i startupów.</p>
  </div>
</section>

<nav class="mini-nav" data-mini-nav aria-label="Usługi na tej stronie">
  <div class="mini-nav-inner">
    <a href="#microsoft-365">Microsoft 365</a>
    <a href="#websites">Web Design</a>
    <a href="#it-support">Wsparcie IT</a>
    <a href="#data-analytics">Analiza Danych</a>
    <a href="#additional-services">Usługi Dodatkowe</a>
  </div>
</nav>

<section class="detail-service section-alt" id="microsoft-365">
  <div class="container detail-grid">
    <div class="detail-copy">
      {MARK_M365}
      <h2 style="margin-top:14px;">Microsoft 365 zarządzane jak należy</h2>
      <p>Od kont użytkowników i licencji po bezpieczeństwo, uprawnienia i zarządzanie urządzeniami — Cevano pomaga małym firmom w pełni wykorzystać Microsoft 365, zachowując uporządkowane i bezpieczne środowisko, bez potrzeby zatrudniania administratora na pełen etat.</p>
      <ul class="check-list">
        {check_items([
            "Konta użytkowników, wdrażanie i wyrejestrowywanie",
            "Licencjonowanie Microsoft 365",
            "Grupy zabezpieczeń i zarządzanie uprawnieniami",
            "Konfiguracja bezpieczeństwa Microsoft 365",
            "Konfiguracja urządzeń i Microsoft Intune",
            "Wsparcie SharePoint, OneDrive i Microsoft Teams",
            "Migracje Microsoft 365 w uzasadnionych przypadkach",
        ])}
      </ul>
      <a class="btn btn-outline service-ask" href="contact.html?service=m365">Zapytaj o Microsoft 365</a>
    </div>
    <div class="panel">
      <h3>Jak to wygląda w praktyce</h3>
      <ul>
        <li>Nowy pracownik ma odpowiedni dostęp od pierwszego dnia</li>
        <li>Konta osób odchodzących są prawidłowo zamykane</li>
        <li>Firmowe pliki są uporządkowane i łatwe do znalezienia w SharePoint</li>
        <li>Urządzenia są konfigurowane spójnie za pomocą Intune</li>
        <li>Licencje odpowiadają rzeczywistym potrzebom zespołu</li>
      </ul>
    </div>
  </div>
</section>

<section class="detail-service" id="websites">
  <div class="container detail-grid reverse">
    <div class="detail-copy">
      {MARK_WEB}
      <h2 style="margin-top:14px;">Strony internetowe, które pomagają Twojej firmie się wyróżnić.</h2>
      <p>Nowoczesne, responsywne strony internetowe i landing page, które jasno przedstawiają Twoją ofertę i ułatwiają klientom kontakt. Zajmujemy się całością — od projektu i wykonania strony po hosting, domenę i konfigurację poczty firmowej.</p>
      <ul class="check-list">
        {check_items([
            "Jednostronicowe landing page",
            "Strony internetowe dla małych firm",
            "Responsywny design na telefony, tablety i komputery",
            "Formularze kontaktowe wysyłające zapytania bezpośrednio na Twoją skrzynkę",
            "Konfiguracja hostingu i uruchomienie strony",
            "Konfiguracja domeny, DNS i poczty firmowej",
        ])}
      </ul>
      <a class="btn btn-outline service-ask" href="contact.html?service=website">Zapytaj o stronę internetową</a>
    </div>
    <div class="panel">
      <h3>Strony internetowe dopasowane do Twojej firmy</h3>
      <ul>
        <li>Profesjonalna strona, która jasno przedstawia Twoją ofertę</li>
        <li>Landing page dla nowej usługi, produktu lub kampanii</li>
        <li>Prosty sposób, aby potencjalni klienci mogli się z Tobą skontaktować</li>
        <li>Kompleksowa konfiguracja domeny, hostingu i poczty firmowej</li>
      </ul>
    </div>
  </div>
</section>

<section class="detail-service section-alt" id="it-support">
  <div class="container detail-grid">
    <div>{MARK_SUPPORT}
      <h2 style="margin-top:14px;">Wsparcie IT, dzięki któremu Twoja firma działa sprawnie</h2>
      <p>Niezawodne, praktyczne wsparcie IT dla technologii, na których Twoja firma opiera się każdego dnia. Od rozwiązywania problemów i konfiguracji urządzeń po przeprowadzki biura i doradztwo techniczne — dbamy o to, by Twoje systemy działały, a zespół mógł spokojnie pracować.</p>
      <ul class="check-list">
        {check_items([
            "Ogólne wsparcie IT i rozwiązywanie problemów",
            "Wsparcie sprzętu i oprogramowania",
            "Instalacja i konfiguracja komputerów i laptopów",
            "Wsparcie IT na miejscu i zdalnie",
            "Przeprowadzki biura i przeniesienie infrastruktury IT",
            "Praktyczne doradztwo IT",
        ])}
      </ul>
      <a class="btn btn-outline service-ask" href="contact.html?service=it-support">Zapytaj o wsparcie IT</a>
    </div>
    <div class="panel">
      <h3>Jak możemy pomóc</h3>
      <ul>
        <li>Konfiguracja nowych użytkowników, komputerów, laptopów i kont Microsoft 365</li>
        <li>Rozwiązywanie problemów z Microsoft 365, pocztą, drukarkami, Wi-Fi i siecią</li>
        <li>Naprawa powtarzających się problemów IT i ustalanie ich przyczyny</li>
        <li>Uruchomienie i wsparcie IT w nowym lub przeniesionym biurze</li>
        <li>Praktyczne porady dotyczące sprzętu, oprogramowania i usprawnień IT</li>
      </ul>
    </div>
  </div>
</section>

<section class="detail-service" id="data-analytics">
  <div class="container detail-grid reverse">
    <div class="detail-copy">
      {MARK_DATA}
      <h2 style="margin-top:14px;">Wykorzystaj dane, aby podejmować lepsze decyzje biznesowe.</h2>
      <p>Pomagamy małym firmom przekształcać dane z Excela, systemów biznesowych i innych źródeł w przejrzyste dashboardy i raporty Power BI. Dzięki temu łatwiej zrozumiesz wyniki swojej firmy, dostrzeżesz ważne trendy i podejmiesz bardziej świadome decyzje.</p>
      <p class="trust-badge">{ICON_CERT}Microsoft Certified: Power BI Data Analyst Associate (PL-300)</p>
      <ul class="check-list">
        {check_items([
            "Analiza danych i Business Intelligence",
            "Dashboardy Power BI i wizualizacja danych",
            "Raportowanie KPI i wyników biznesowych",
            "Przygotowanie i przekształcanie danych za pomocą Power Query",
            "Zamiana arkuszy Excel i danych firmowych w praktyczne informacje",
            "Raporty na potrzeby spotkań zarządczych i przeglądów biznesowych",
        ])}
      </ul>
      <a class="btn btn-outline service-ask" href="contact.html?service=data">Zapytaj o Power BI</a>
    </div>
    <div class="panel">
      <h3>Jak możemy pomóc?</h3>
      <ul>
        <li>Zebranie danych sprzedażowych, finansowych lub operacyjnych w jednym przejrzystym dashboardzie</li>
        <li>Zastąpienie ręcznie przygotowywanych raportów Excel automatycznym raportowaniem w Power BI</li>
        <li>Monitorowanie najważniejszych wskaźników KPI Twojej firmy</li>
        <li>Łączenie danych z różnych systemów w jednym raporcie</li>
        <li>Przygotowanie czytelnych raportów na potrzeby spotkań i podejmowania decyzji biznesowych</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-alt" id="additional-services">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Dodatkowe Usługi IT</span>
      <h2>Wszystko, czego potrzebujesz, aby Twoja firma działała sprawnie i bezpiecznie.</h2>
      <p>Oprócz naszych głównych usług oferujemy również dodatkowe wsparcie techniczne, pomagając małym firmom w zarządzaniu infrastrukturą sieciową, sprzętem IT, technologią biurową i usługami internetowymi.</p>
    </div>
    <div class="subservice-grid">
      <div class="subservice-card">
        {MARK_NET}
        <h3>Sieci Komputerowe i AV</h3>
        <p>Niezawodna sieć i nowoczesne rozwiązania audiowizualne w Twoim biurze.</p>
        <ul>
          <li>Konfiguracja sieci firmowych i Wi-Fi</li>
          <li>Diagnostyka i rozwiązywanie problemów z siecią</li>
          <li>Infrastruktura sieciowa biura</li>
          <li>Systemy AV i wideokonferencyjne w salach spotkań</li>
          <li>Okablowanie sieciowe i szafy teleinformatyczne</li>
        </ul>
      </div>
      <div class="subservice-card">
        {MARK_ASSETS}
        <h3>Sprzęt IT i Dokumentacja</h3>
        <p>Pełna wiedza o posiadanym sprzęcie, systemach i infrastrukturze IT.</p>
        <ul>
          <li>Inwentaryzacja sprzętu i urządzeń IT</li>
          <li>Ewidencja sprzętu i oprogramowania</li>
          <li>Dokumentacja infrastruktury i systemów IT</li>
          <li>Dokumentacja techniczna na potrzeby audytów i przeglądów</li>
          <li>Ewidencja sprzętu i monitorowanie jego cyklu życia</li>
        </ul>
      </div>
      <div class="subservice-card">
        {MARK_DOMAIN}
        <h3>Domeny i Poczta Firmowa</h3>
        <p>Podstawowe usługi niezbędne do działania Twojej strony internetowej i komunikacji firmowej.</p>
        <ul>
          <li>Rejestracja i konfiguracja domen</li>
          <li>Zarządzanie DNS i rozwiązywanie problemów z konfiguracją</li>
          <li>Konfiguracja poczty firmowej</li>
          <li>Integracja domen i poczty z Microsoft 365</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Nie wiesz, która usługa będzie najlepsza dla Twojej firmy?</h2>
        <p>Powiedz nam, w czym możemy Ci pomóc, a znajdziemy rozwiązanie dopasowane do Twoich potrzeb.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Skontaktuj się z nami</a>
    </div>
  </div>
</section>
'''

write("pl/services.html", page(
    "pl", "", "../", "services",
    "Usługi | Microsoft 365, strony internetowe, wsparcie IT i analiza danych — Cevano",
    "Administracja Microsoft 365, strony internetowe i landing page, wsparcie IT oraz analiza danych Power BI dla małych firm, wyjaśnione prostym językiem.",
    "services.html", "services.html", body_services_pl, alt_href="../services.html"
))
