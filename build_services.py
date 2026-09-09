# -*- coding: utf-8 -*-
from build import *

# ================================================================
# SERVICES — EN
# ================================================================
body_services_en = f'''
<section class="page-hero">
  <div class="container">
    <h1>Practical IT, properly managed Microsoft 365, and data you can use</h1>
    <p>Three core services that work together — plus the everyday extras that keep a small office running.</p>
  </div>
</section>

<nav class="mini-nav" data-mini-nav aria-label="Services on this page">
  <div class="mini-nav-inner">
    <a href="#it-support">IT Support</a>
    <a href="#microsoft-365">Microsoft 365</a>
    <a href="#data-analytics">Data Analytics</a>
    <a href="#additional-services">Additional Services</a>
  </div>
</nav>

<section class="detail-service" id="it-support">
  <div class="container detail-grid">
    <div>{MARK_SUPPORT}
      <h2 style="margin-top:14px;">IT Support</h2>
      <p>Reliable IT support without the complexity. We handle the day-to-day technology issues that get in the way of running your business — troubleshooting, setup, and advice you can actually understand.</p>
      <ul class="check-list">
        {check_items([
            "General IT support and troubleshooting",
            "Hardware and software support",
            "PC and laptop setup and configuration",
            "Office IT support and remote support",
            "Office moves and technical relocation setup",
            "Practical IT advice and consultancy",
        ])}
      </ul>
    </div>
    <div class="panel">
      <h4>Common requests we help with</h4>
      <ul>
        <li>Setting up a new starter's laptop and accounts</li>
        <li>Fixing recurring printer or network issues</li>
        <li>Technical setup for a new or moving office</li>
        <li>Ad-hoc remote support when something isn't working</li>
        <li>Plain-English advice before buying new hardware or software</li>
      </ul>
    </div>
  </div>
</section>

<section class="detail-service section-alt" id="microsoft-365">
  <div class="container detail-grid reverse">
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
    </div>
    <div class="panel">
      <h4>What this looks like in practice</h4>
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

<section class="detail-service" id="data-analytics">
  <div class="container detail-grid">
    <div>
      {MARK_DATA}
      <h2 style="margin-top:14px;">Make better decisions with your data.</h2>
      <p>Cevano helps small businesses turn data from Excel, systems and other sources into clear Power BI dashboards and meaningful business insight — explained in plain terms, not jargon.</p>
      <ul class="check-list">
        {check_items([
            "Data analysis and business intelligence",
            "Power BI dashboards and data visualisation",
            "KPI reporting for your business",
            "Data transformation using Power Query",
            "Turning spreadsheets into useful insight",
            "Building presentations for meetings and reports",
        ])}
      </ul>
    </div>
    <div class="panel">
      <h4>Example uses</h4>
      <ul>
        <li>A single dashboard showing sales performance at a glance</li>
        <li>Reports that refresh automatically, saving hours of manual work each month</li>
        <li>Clear visuals for a board meeting or investor update</li>
        <li>Combining data from more than one system into one view</li>
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
        <h3>Domains &amp; Online Services</h3>
        <p>The foundations behind your website and email.</p>
        <ul>
          <li>Domain name services and configuration</li>
          <li>DNS-related support</li>
          <li>Business email and domain setup</li>
          <li>Web / landing page design</li>
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
    "Services | IT Support, Microsoft 365 &amp; Data Analytics — Cevano",
    "IT support, Microsoft 365 administration and Power BI data analytics for small businesses, explained in plain English.",
    "services.html", "services.html", body_services_en, alt_href="pl/services.html"
))

# ================================================================
# SERVICES — PL
# ================================================================
body_services_pl = f'''
<section class="page-hero">
  <div class="container">
    <h1>Praktyczne IT, dobrze zarządzany Microsoft 365 i dane, z których można korzystać</h1>
    <p>Trzy główne usługi, które działają razem — oraz codzienne wsparcie, które utrzymuje małe biuro w sprawnym działaniu.</p>
  </div>
</section>

<nav class="mini-nav" data-mini-nav aria-label="Usługi na tej stronie">
  <div class="mini-nav-inner">
    <a href="#it-support">Wsparcie IT</a>
    <a href="#microsoft-365">Microsoft 365</a>
    <a href="#data-analytics">Analiza danych</a>
    <a href="#additional-services">Usługi dodatkowe</a>
  </div>
</nav>

<section class="detail-service" id="it-support">
  <div class="container detail-grid">
    <div>{MARK_SUPPORT}
      <h2 style="margin-top:14px;">Wsparcie IT</h2>
      <p>Niezawodne wsparcie IT bez zbędnej złożoności. Zajmujemy się codziennymi problemami technologicznymi, które przeszkadzają w prowadzeniu firmy — rozwiązywaniem problemów, konfiguracją i doradztwem w zrozumiałym języku.</p>
      <ul class="check-list">
        {check_items([
            "Ogólne wsparcie IT i rozwiązywanie problemów",
            "Wsparcie sprzętowe i programowe",
            "Konfiguracja komputerów i laptopów",
            "Wsparcie IT w biurze oraz wsparcie zdalne",
            "Przeprowadzki biura i techniczna organizacja nowego miejsca",
            "Praktyczne doradztwo IT",
        ])}
      </ul>
    </div>
    <div class="panel">
      <h4>Typowe zgłoszenia, z którymi pomagamy</h4>
      <ul>
        <li>Konfiguracja laptopa i kont dla nowego pracownika</li>
        <li>Naprawa powtarzających się problemów z drukarką lub siecią</li>
        <li>Techniczna organizacja nowego lub przenoszonego biura</li>
        <li>Doraźne wsparcie zdalne, gdy coś nie działa</li>
        <li>Rzeczowe porady przed zakupem nowego sprzętu lub oprogramowania</li>
      </ul>
    </div>
  </div>
</section>

<section class="detail-service section-alt" id="microsoft-365">
  <div class="container detail-grid reverse">
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
    </div>
    <div class="panel">
      <h4>Jak to wygląda w praktyce</h4>
      <ul>
        <li>Nowy pracownik ma odpowiedni dostęp od pierwszego dnia</li>
        <li>Osoby odchodzące są prawidłowo wyrejestrowywane, bez otwartych kont</li>
        <li>Firmowe pliki są uporządkowane i łatwe do znalezienia w SharePoint</li>
        <li>Urządzenia są konfigurowane spójnie za pomocą Intune</li>
        <li>Licencje odpowiadają rzeczywistym potrzebom zespołu</li>
      </ul>
    </div>
  </div>
</section>

<section class="detail-service" id="data-analytics">
  <div class="container detail-grid">
    <div>
      {MARK_DATA}
      <h2 style="margin-top:14px;">Podejmuj lepsze decyzje dzięki danym</h2>
      <p>Cevano pomaga małym firmom przekształcać dane z Excela, systemów i innych źródeł w przejrzyste pulpity Power BI oraz konkretne wnioski biznesowe — wyjaśnione prostym językiem, bez żargonu.</p>
      <ul class="check-list">
        {check_items([
            "Analiza danych i business intelligence",
            "Pulpity Power BI i wizualizacja danych",
            "Raportowanie KPI dla Twojej firmy",
            "Przekształcanie danych za pomocą Power Query",
            "Zamiana arkuszy kalkulacyjnych w użyteczne wnioski",
            "Budowanie prezentacji na spotkania i raporty",
        ])}
      </ul>
    </div>
    <div class="panel">
      <h4>Przykładowe zastosowania</h4>
      <ul>
        <li>Jeden pulpit pokazujący wyniki sprzedaży na pierwszy rzut oka</li>
        <li>Raporty aktualizujące się automatycznie, oszczędzające godziny pracy każdego miesiąca</li>
        <li>Przejrzyste wizualizacje na spotkanie zarządu lub dla inwestora</li>
        <li>Połączenie danych z kilku systemów w jednym widoku</li>
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
        <h3>Domeny i usługi online</h3>
        <p>Podstawy działania Twojej strony internetowej i poczty.</p>
        <ul>
          <li>Usługi domenowe i konfiguracja</li>
          <li>Wsparcie związane z DNS</li>
          <li>Konfiguracja poczty firmowej i domeny</li>
          <li>Projektowanie stron i landing page'y</li>
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
    "Usługi | Wsparcie IT, Microsoft 365 i analiza danych — Cevano",
    "Wsparcie IT, administracja Microsoft 365 oraz analiza danych Power BI dla małych firm, wyjaśnione prostym językiem.",
    "services.html", "services.html", body_services_pl, alt_href="../services.html"
))
