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
      <span class="kicker">Additional support</span>
      <h2>Networking, assets and domains</h2>
      <p>Secondary services we provide alongside our core offering.</p>
    </div>
    <div class="subservice-grid">
      <div class="subservice-card">
        {MARK_NET}
        <h3>Networking &amp; AV</h3>
        <p>Keeping your office connected and your meeting rooms working.</p>
        <ul>
          <li>Business networking and Wi-Fi</li>
          <li>Network troubleshooting</li>
          <li>Office connectivity</li>
          <li>AV systems and meeting room technology</li>
          <li>Comms cabinets and cabling-related support</li>
        </ul>
      </div>
      <div class="subservice-card">
        {MARK_ASSETS}
        <h3>IT Assets &amp; Documentation</h3>
        <p>Knowing what you have, and where it is.</p>
        <ul>
          <li>IT asset and device inventories</li>
          <li>Technical documentation</li>
          <li>Documentation to support audits</li>
          <li>Asset tracking</li>
        </ul>
      </div>
      <div class="subservice-card">
        {MARK_DOMAIN}
        <h3>Domains &amp; Email</h3>
        <p>The foundations behind your website and email.</p>
        <ul>
          <li>Domain name services and configuration</li>
          <li>DNS-related support</li>
          <li>Business email and domain setup</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Not sure which service you need?</h2>
        <p>Tell us what's going on and we'll point you in the right direction.</p>
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
      <h2 style="margin-top:14px;">Zamień dane w lepsze decyzje biznesowe</h2>
      <p>Pomagamy małym firmom przekształcać dane z Excela, systemów biznesowych i innych źródeł w przejrzyste, użyteczne pulpity i raporty Power BI. Sprawiamy, że Twoje dane są łatwiejsze do zrozumienia, co pomaga śledzić wyniki, dostrzegać trendy i podejmować lepiej przemyślane decyzje.</p>
      <p class="trust-badge">{ICON_CERT}Certyfikat Microsoft Certified: Power BI Data Analyst Associate (PL-300)</p>
      <ul class="check-list">
        {check_items([
            "Analiza danych i business intelligence",
            "Pulpity Power BI i wizualizacja danych",
            "Raportowanie KPI i wyników",
            "Przekształcanie i przygotowanie danych w Power Query",
            "Zamiana arkuszy i danych biznesowych w użyteczne wnioski",
            "Raporty przygotowane na spotkania zarządu i przeglądy biznesowe",
        ])}
      </ul>
      <a class="btn btn-outline service-ask" href="contact.html?service=data">Zapytaj o Power BI</a>
    </div>
    <div class="panel">
      <h3>Jak możemy pomóc</h3>
      <ul>
        <li>Zebranie danych sprzedażowych, finansowych lub operacyjnych w jednym przejrzystym pulpicie</li>
        <li>Zastąpienie ręcznych raportów w Excelu zautomatyzowanymi raportami Power BI</li>
        <li>Śledzenie KPI, które są najważniejsze dla Twojej firmy</li>
        <li>Łączenie danych z wielu źródeł w jednym widoku</li>
        <li>Przygotowanie przejrzystych raportów na spotkania zarządu i przeglądy biznesowe</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-alt" id="additional-services">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Dodatkowe wsparcie</span>
      <h2>Sieci, zasoby i domeny</h2>
      <p>Usługi dodatkowe, świadczone obok naszej głównej oferty.</p>
    </div>
    <div class="subservice-grid">
      <div class="subservice-card">
        {MARK_NET}
        <h3>Sieci i AV</h3>
        <p>Dbamy o łączność w biurze i działanie sal spotkań.</p>
        <ul>
          <li>Sieci firmowe i Wi-Fi</li>
          <li>Rozwiązywanie problemów sieciowych</li>
          <li>Łączność biurowa</li>
          <li>Systemy AV i technologia sal spotkań</li>
          <li>Szafy komunikacyjne i wsparcie związane z okablowaniem</li>
        </ul>
      </div>
      <div class="subservice-card">
        {MARK_ASSETS}
        <h3>Zasoby IT i dokumentacja</h3>
        <p>Wiedza o tym, co posiadasz i gdzie się to znajduje.</p>
        <ul>
          <li>Inwentaryzacja zasobów i urządzeń IT</li>
          <li>Dokumentacja techniczna</li>
          <li>Dokumentacja wspierająca audyty</li>
          <li>Śledzenie zasobów</li>
        </ul>
      </div>
      <div class="subservice-card">
        {MARK_DOMAIN}
        <h3>Domeny i poczta</h3>
        <p>Podstawy działania Twojej strony internetowej i poczty.</p>
        <ul>
          <li>Usługi domenowe i konfiguracja</li>
          <li>Wsparcie związane z DNS</li>
          <li>Konfiguracja poczty firmowej i domeny</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Nie wiesz, której usługi potrzebujesz?</h2>
        <p>Opisz, z czym się mierzysz, a wskażemy Ci właściwy kierunek.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Skontaktuj się</a>
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
