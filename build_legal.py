# -*- coding: utf-8 -*-
from build import *

FLAG_EN = '<span class="placeholder-flag">Placeholder — to be completed by Cevano</span>'
FLAG_PL = '<span class="placeholder-flag">Do uzupełnienia przez Cevano</span>'

# ================================================================
# PRIVACY POLICY — EN
# ================================================================
body_privacy_en = f'''
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a> / Privacy &amp; Cookie Policy</div>
    <h1>Privacy &amp; Cookie Policy</h1>
    <p>How Cevano IT Solutions collects, uses and protects your information.</p>
  </div>
</section>

<section class="section">
  <div class="container legal-content">
    <p><em>Last updated: {FLAG_EN} (insert date this policy was published).</em></p>

    <h2>Who we are</h2>
    <p>Cevano IT Solutions ("Cevano", "we", "us") provides IT support, Microsoft 365 and data analytics services to small businesses and individuals. This policy explains how we handle personal data collected through this website and in the course of providing our services.</p>
    <p>Registered company details: Cevano IT Solutions, company number 17428300. Registered office: 1 Gresham Drive, West Hunsbury, Northampton, NN4 9SB.</p>

    <h2>Data we collect</h2>
    <p>When you use our contact form or email us directly, we collect the information you choose to provide, which may include your name, company name, email address, phone number, and the details of your enquiry. We do not ask for more information than we need to respond to you.</p>

    <h2>How we use your data</h2>
    <ul>
      <li>To respond to enquiries submitted through the contact form or by email</li>
      <li>To provide, manage and administer any services you engage us for</li>
      <li>To meet our legal and accounting obligations</li>
    </ul>
    <p>We do not sell your personal data, and we do not use it for unrelated marketing without your consent.</p>

    <h2>Legal basis for processing</h2>
    <p>We process contact form and enquiry data on the basis of your consent and our legitimate interest in responding to enquiries about our services. Where we provide services to you, we process data as necessary to perform that contract.</p>

    <h2>How long we keep your data</h2>
    <p>We keep enquiry and client data for as long as reasonably necessary to respond to you, provide our services, and meet any legal or accounting requirements, after which it is deleted or anonymised.</p>

    <h2>Cookies</h2>
    <p>This website uses a limited number of cookies:</p>
    <ul>
      <li><strong>Essential cookies</strong> — needed for the website to function correctly (for example, remembering your dark/light theme preference and that you've seen the cookie notice). These are stored in your browser and are not shared with third parties.</li>
      <li><strong>Analytics cookies</strong> {FLAG_EN} (confirm here which analytics service, if any, is in use — for example Google Analytics or Plausible — and update this section to match).</li>
    </ul>
    <p>You can control or delete cookies through your browser settings at any time.</p>

    <h2>Sharing your data</h2>
    <p>We do not sell your personal data, and we only share it with the specific service providers needed to run this website and respond to your enquiry:</p>
    <ul>
      <li><strong>Cloudflare</strong> — hosts this website and processes web traffic (including standard technical data such as IP addresses) as part of delivering the site and protecting it from abuse. Cloudflare acts as our infrastructure provider.</li>
      <li><strong>Resend</strong> — the transactional email service used to deliver contact form submissions to our inbox. When you submit the contact form, your name, email address, and message pass through Resend in order to reach us.</li>
      <li><strong>Microsoft 365 / Exchange Online</strong> — our business email is hosted with Microsoft 365. Enquiries sent through the contact form, or emailed to us directly, are ultimately received and stored in our Microsoft 365 mailbox.</li>
    </ul>
    <p>We don't collect or store visitor IP addresses ourselves for contact form submissions. Cloudflare, as our hosting and security provider, processes standard connection data (such as IP addresses) as part of normal web infrastructure operation and abuse prevention — this is not something Cevano separately collects, stores, or has direct access to beyond aggregate, anonymised traffic statistics.</p>
    <p>We otherwise only share data where required by law.</p>

    <h2>Your rights</h2>
    <p>Under UK data protection law, you have the right to ask what personal data we hold about you, to request corrections, to ask us to delete it, and to object to certain uses. To exercise any of these rights, contact us at <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a>.</p>
    <p>You also have the right to complain to the Information Commissioner's Office (ICO) if you believe your data has been mishandled: <a href="https://ico.org.uk" target="_blank" rel="noopener">ico.org.uk</a>.</p>

    <h2>Contact us</h2>
    <p>If you have questions about this policy or how your data is handled, email <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a>.</p>
  </div>
</section>
'''

write("legal/privacy-policy.html", page(
    "en", "../", "../", "legal",
    "Privacy &amp; Cookie Policy | Cevano IT Solutions",
    "How Cevano IT Solutions collects, uses and protects personal data, and how cookies are used on this website.",
    "legal/privacy-policy.html", "legal/privacy-policy.html", body_privacy_en, alt_href="../pl/legal/privacy-policy.html"
))

# ================================================================
# TERMS — EN
# ================================================================
body_terms_en = f'''
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a> / Terms &amp; Conditions</div>
    <h1>Terms &amp; Conditions</h1>
    <p>The terms that apply to use of this website and enquiries made through it.</p>
  </div>
</section>

<section class="section">
  <div class="container legal-content">
    <p><em>Last updated: {FLAG_EN} (insert date this policy was published).</em></p>

    <h2>About these terms</h2>
    <p>These terms apply to your use of this website (cevano.co.uk), operated by Cevano IT Solutions. They do not constitute a service contract — the specific terms for any IT support, Microsoft 365 or data analytics work will be agreed with you separately before work begins.</p>

    <h2>Company information</h2>
    <p>Cevano IT Solutions. Registered company number: 17428300. Registered office: 1 Gresham Drive, West Hunsbury, Northampton, NN4 9SB. VAT number (if applicable): {FLAG_EN}.</p>

    <h2>Use of this website</h2>
    <p>This website is provided for general information about our services. While we take care to keep it accurate and up to date, we make no guarantees about completeness or fitness for a particular purpose, and content may change without notice.</p>

    <h2>Enquiries and quotations</h2>
    <p>Submitting the contact form or emailing us does not create a binding agreement. Any quotation, proposal or scope of work will be confirmed separately in writing before chargeable work begins.</p>

    <h2>Intellectual property</h2>
    <p>The Cevano name, logo and website content are the property of Cevano IT Solutions unless otherwise stated, and may not be reproduced without permission.</p>

    <h2>Limitation of liability</h2>
    <p>We aim to provide accurate information on this website, but we do not accept liability for loss arising from reliance on website content alone. Liability relating to actual service engagements will be set out in the separate terms agreed for that work.</p>

    <h2>Governing law</h2>
    <p>These terms are governed by the laws of England and Wales.</p>

    <h2>Contact</h2>
    <p>Questions about these terms can be sent to <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a>.</p>
  </div>
</section>
'''

write("legal/terms.html", page(
    "en", "../", "../", "legal",
    "Terms &amp; Conditions | Cevano IT Solutions",
    "The terms and conditions that apply to the use of the Cevano IT Solutions website.",
    "legal/terms.html", "legal/terms.html", body_terms_en, alt_href="../pl/legal/terms.html"
))

# ================================================================
# PRIVACY POLICY — PL
# ================================================================
body_privacy_pl = f'''
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Strona główna</a> / Polityka prywatności i cookies</div>
    <h1>Polityka prywatności i cookies</h1>
    <p>Jak Cevano IT Solutions gromadzi, wykorzystuje i chroni Twoje dane.</p>
  </div>
</section>

<section class="section">
  <div class="container legal-content">
    <p><em>Ostatnia aktualizacja: {FLAG_PL} (uzupełnić datę publikacji).</em></p>

    <h2>Kim jesteśmy</h2>
    <p>Cevano IT Solutions („Cevano”, „my”) świadczy usługi wsparcia IT, Microsoft 365 oraz analizy danych dla małych firm i osób prywatnych. Niniejsza polityka wyjaśnia, w jaki sposób przetwarzamy dane osobowe zbierane za pośrednictwem tej strony internetowej oraz w ramach świadczenia naszych usług.</p>
    <p>Dane rejestrowe firmy: Cevano IT Solutions, numer rejestracyjny 17428300. Siedziba: 1 Gresham Drive, West Hunsbury, Northampton, NN4 9SB.</p>

    <h2>Jakie dane zbieramy</h2>
    <p>Korzystając z formularza kontaktowego lub pisząc do nas bezpośrednio, zbieramy dane, które zdecydujesz się podać — mogą to być imię i nazwisko, nazwa firmy, adres e-mail, numer telefonu oraz treść zapytania. Nie prosimy o więcej informacji, niż jest to potrzebne do udzielenia odpowiedzi.</p>

    <h2>Jak wykorzystujemy Twoje dane</h2>
    <ul>
      <li>Aby odpowiedzieć na zapytania przesłane przez formularz kontaktowy lub e-mail</li>
      <li>Aby świadczyć, obsługiwać i administrować usługami, które nam zlecisz</li>
      <li>Aby wypełniać nasze obowiązki prawne i księgowe</li>
    </ul>
    <p>Nie sprzedajemy Twoich danych osobowych i nie wykorzystujemy ich do niepowiązanych działań marketingowych bez Twojej zgody.</p>

    <h2>Podstawa prawna przetwarzania</h2>
    <p>Dane z formularza kontaktowego przetwarzamy na podstawie Twojej zgody oraz naszego prawnie uzasadnionego interesu polegającego na odpowiadaniu na zapytania dotyczące naszych usług. W przypadku świadczenia usług dane przetwarzamy w zakresie niezbędnym do wykonania umowy.</p>

    <h2>Jak długo przechowujemy dane</h2>
    <p>Dane dotyczące zapytań i klientów przechowujemy tak długo, jak jest to zasadnie konieczne do udzielenia odpowiedzi, świadczenia usług oraz spełnienia wymogów prawnych lub księgowych, po czym są usuwane lub anonimizowane.</p>

    <h2>Pliki cookie</h2>
    <p>Ta strona wykorzystuje ograniczoną liczbę plików cookie:</p>
    <ul>
      <li><strong>Niezbędne pliki cookie</strong> — konieczne do prawidłowego działania strony (np. zapamiętywanie wybranego motywu jasnego/ciemnego oraz informacji o wyświetleniu powiadomienia o cookies). Są przechowywane w Twojej przeglądarce i nie są udostępniane podmiotom trzecim.</li>
      <li><strong>Analityczne pliki cookie</strong> {FLAG_PL} (potwierdzić, z jakiego narzędzia analitycznego korzystamy, np. Google Analytics lub Plausible, i zaktualizować tę sekcję).</li>
    </ul>
    <p>W każdej chwili możesz kontrolować lub usuwać pliki cookie w ustawieniach swojej przeglądarki.</p>

    <h2>Udostępnianie danych</h2>
    <p>Nie sprzedajemy Twoich danych osobowych i udostępniamy je wyłącznie dostawcom usług niezbędnym do prowadzenia tej strony i odpowiedzi na Twoje zapytanie:</p>
    <ul>
      <li><strong>Cloudflare</strong> — hostuje tę stronę internetową i przetwarza ruch sieciowy (w tym standardowe dane techniczne, takie jak adresy IP) w ramach udostępniania strony i ochrony jej przed nadużyciami. Cloudflare pełni rolę naszego dostawcy infrastruktury.</li>
      <li><strong>Resend</strong> — usługa transakcyjnej wysyłki e-maili wykorzystywana do dostarczania zgłoszeń z formularza kontaktowego na naszą skrzynkę. Wysyłając formularz kontaktowy, Twoje imię i nazwisko, adres e-mail oraz wiadomość przechodzą przez Resend, aby do nas dotrzeć.</li>
      <li><strong>Microsoft 365 / Exchange Online</strong> — nasza firmowa poczta jest hostowana w Microsoft 365. Zapytania wysłane przez formularz kontaktowy lub bezpośrednio e-mailem trafiają ostatecznie do naszej skrzynki Microsoft 365.</li>
    </ul>
    <p>Sami nie zbieramy ani nie przechowujemy adresów IP odwiedzających w związku ze zgłoszeniami z formularza kontaktowego. Cloudflare, jako nasz dostawca hostingu i zabezpieczeń, przetwarza standardowe dane połączenia (takie jak adresy IP) w ramach normalnego funkcjonowania infrastruktury internetowej i ochrony przed nadużyciami — nie jest to coś, co Cevano samodzielnie zbiera, przechowuje lub do czego ma bezpośredni dostęp, poza zagregowanymi, zanonimizowanymi statystykami ruchu.</p>
    <p>Poza tym udostępniamy dane wyłącznie w sytuacjach wymaganych przez prawo.</p>

    <h2>Twoje prawa</h2>
    <p>Zgodnie z brytyjskim prawem o ochronie danych masz prawo dowiedzieć się, jakie dane na Twój temat przechowujemy, zażądać ich poprawienia, usunięcia lub sprzeciwić się określonym sposobom ich wykorzystania. Aby skorzystać z tych praw, napisz do nas na adres <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a>.</p>
    <p>Masz również prawo złożyć skargę do brytyjskiego Information Commissioner's Office (ICO), jeśli uważasz, że Twoje dane zostały nieprawidłowo przetworzone: <a href="https://ico.org.uk" target="_blank" rel="noopener">ico.org.uk</a>.</p>

    <h2>Kontakt</h2>
    <p>Pytania dotyczące niniejszej polityki prosimy kierować na adres <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a>.</p>
  </div>
</section>
'''

write("pl/legal/privacy-policy.html", page(
    "pl", "../", "../../", "legal",
    "Polityka prywatności i cookies | Cevano IT Solutions",
    "Jak Cevano IT Solutions gromadzi, wykorzystuje i chroni dane osobowe oraz jak wykorzystywane są pliki cookie na tej stronie.",
    "legal/privacy-policy.html", "legal/privacy-policy.html", body_privacy_pl, alt_href="../../legal/privacy-policy.html"
))

# ================================================================
# TERMS — PL
# ================================================================
body_terms_pl = f'''
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Strona główna</a> / Regulamin</div>
    <h1>Regulamin</h1>
    <p>Warunki korzystania z tej strony internetowej oraz zapytań składanych za jej pośrednictwem.</p>
  </div>
</section>

<section class="section">
  <div class="container legal-content">
    <p><em>Ostatnia aktualizacja: {FLAG_PL} (uzupełnić datę publikacji).</em></p>

    <h2>O niniejszym regulaminie</h2>
    <p>Niniejszy regulamin dotyczy korzystania z tej strony internetowej (cevano.co.uk), prowadzonej przez Cevano IT Solutions. Nie stanowi on umowy o świadczenie usług — szczegółowe warunki dla konkretnych prac związanych ze wsparciem IT, Microsoft 365 czy analizą danych będą ustalane odrębnie przed rozpoczęciem prac.</p>

    <h2>Dane firmy</h2>
    <p>Cevano IT Solutions. Numer rejestracyjny firmy: 17428300. Siedziba: 1 Gresham Drive, West Hunsbury, Northampton, NN4 9SB. Numer VAT (jeśli dotyczy): {FLAG_PL}.</p>

    <h2>Korzystanie ze strony</h2>
    <p>Ta strona ma charakter informacyjny i przedstawia nasze usługi. Dokładamy starań, aby treści były aktualne i rzetelne, jednak nie gwarantujemy ich kompletności ani przydatności do konkretnego celu, a zawartość może ulec zmianie bez wcześniejszego powiadomienia.</p>

    <h2>Zapytania i wyceny</h2>
    <p>Wysłanie formularza kontaktowego lub wiadomości e-mail nie stanowi zawarcia wiążącej umowy. Wszelkie wyceny, propozycje lub zakresy prac zostaną odrębnie potwierdzone pisemnie przed rozpoczęciem odpłatnych prac.</p>

    <h2>Własność intelektualna</h2>
    <p>Nazwa Cevano, logo oraz treści tej strony stanowią własność Cevano IT Solutions, chyba że zaznaczono inaczej, i nie mogą być powielane bez zgody.</p>

    <h2>Ograniczenie odpowiedzialności</h2>
    <p>Staramy się zapewnić dokładność informacji zamieszczonych na tej stronie, jednak nie ponosimy odpowiedzialności za straty wynikające wyłącznie z polegania na jej treści. Odpowiedzialność związana z faktycznie świadczonymi usługami zostanie określona w odrębnych warunkach uzgodnionych dla danego zlecenia.</p>

    <h2>Prawo właściwe</h2>
    <p>Niniejszy regulamin podlega prawu Anglii i Walii.</p>

    <h2>Kontakt</h2>
    <p>Pytania dotyczące regulaminu prosimy kierować na adres <a href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a>.</p>
  </div>
</section>
'''

write("pl/legal/terms.html", page(
    "pl", "../", "../../", "legal",
    "Regulamin | Cevano IT Solutions",
    "Regulamin korzystania ze strony internetowej Cevano IT Solutions.",
    "legal/terms.html", "legal/terms.html", body_terms_pl, alt_href="../../legal/terms.html"
))
