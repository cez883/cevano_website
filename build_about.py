# -*- coding: utf-8 -*-
from build import *

# ================================================================
# ABOUT — EN
# ================================================================
body_about_en = f'''
<section class="page-hero">
  <div class="container">
    <h1>About Cevano IT Solutions</h1>
    <p>An approachable technology partner for small businesses, sole traders and individuals.</p>
  </div>
</section>

<section class="section">
  <div class="container about-layout">
    <div>
      <h2>Practical technology support, without the complexity</h2>
      <p>Cevano IT Solutions provides practical technology support for individuals, sole traders, startups and small businesses. Many of the businesses we work with don't have — and don't need — an internal IT department. What they need is a provider who understands their technology, explains things clearly, and is flexible enough to fit around how they actually work.</p>
      <p>We bring three things together that are usually handled by separate suppliers: everyday IT support, Microsoft 365 administration, and data analytics using Power BI. Keeping these under one roof means fewer handovers, fewer suppliers to manage, and technology decisions that are considered together rather than in isolation.</p>
      <p>Our approach is straightforward: understand the problem, explain the options in plain language, and put in place something practical that actually fits your business — not the most complicated solution available.</p>
    </div>
    <div>
      <div class="panel">
        <h4>What guides how we work</h4>
        <ul>
          <li>Practical solutions over unnecessary complexity</li>
          <li>Clear explanations, without jargon overload</li>
          <li>Flexible support built around your business</li>
          <li>One trusted point of contact for IT, Microsoft 365 and data</li>
          <li>Local roots, with remote support where it makes sense</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container about-layout">
    <div>
      <span class="kicker">Where we work</span>
      <h2>Local support around Northamptonshire, with remote support further afield</h2>
      <p>Cevano works with businesses on-site around Northampton, Kettering, Milton Keynes, Rugby and the surrounding areas of Northamptonshire, Warwickshire and Buckinghamshire. Where a visit isn't necessary, we're also happy to help remotely — many Microsoft 365 and data analytics tasks can be handled just as effectively that way.</p>
      <div class="area-tags">
        <span>Northampton</span><span>Kettering</span><span>Milton Keynes</span><span>Rugby</span>
        <span>Northamptonshire</span><span>Warwickshire</span><span>Buckinghamshire</span><span>Remote UK-wide</span>
      </div>
    </div>
    <div class="about-graphic">{ABOUT_LOCATION_GRAPHIC}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Want to know if we're a good fit for your business?</h2>
        <p>Get in touch and tell us a bit about what you need.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Get in touch</a>
    </div>
  </div>
</section>
'''

write("about.html", page(
    "en", "", "", "about",
    "About Cevano IT Solutions | Practical IT for Small Businesses",
    "Cevano IT Solutions provides practical, approachable IT support, Microsoft 365 management and data analytics for small businesses around Northamptonshire.",
    "about.html", "about.html", body_about_en, alt_href="pl/about.html"
))

# ================================================================
# ABOUT — PL
# ================================================================
body_about_pl = f'''
<section class="page-hero">
  <div class="container">
    <h1>O Cevano IT Solutions</h1>
    <p>Przystępny partner technologiczny dla małych firm, jednoosobowych działalności i osób prywatnych.</p>
  </div>
</section>

<section class="section">
  <div class="container about-layout">
    <div>
      <h2>Praktyczne wsparcie technologiczne bez zbędnej złożoności</h2>
      <p>Cevano IT Solutions zapewnia praktyczne wsparcie technologiczne dla osób prywatnych, jednoosobowych działalności, startupów i małych firm. Wiele firm, z którymi współpracujemy, nie ma — i nie potrzebuje — wewnętrznego działu IT. Potrzebują natomiast dostawcy, który rozumie ich technologię, jasno tłumaczy sprawy techniczne i jest wystarczająco elastyczny, aby dopasować się do sposobu, w jaki faktycznie pracują.</p>
      <p>Łączymy trzy obszary, którymi zwykle zajmują się osobni dostawcy: codzienne wsparcie IT, administrację Microsoft 365 oraz analizę danych z użyciem Power BI. Dzięki temu, że wszystko znajduje się w jednym miejscu, jest mniej przekazywania spraw między firmami, mniej dostawców do koordynowania, a decyzje technologiczne podejmowane są całościowo, a nie w oderwaniu od siebie.</p>
      <p>Nasze podejście jest proste: zrozumieć problem, jasno przedstawić dostępne opcje i wdrożyć rozwiązanie, które faktycznie pasuje do Twojej firmy — a nie najbardziej skomplikowane z dostępnych.</p>
    </div>
    <div>
      <div class="panel">
        <h4>Czym się kierujemy w pracy</h4>
        <ul>
          <li>Praktyczne rozwiązania zamiast zbędnej złożoności</li>
          <li>Jasne wyjaśnienia, bez nadmiaru żargonu</li>
          <li>Elastyczne wsparcie dopasowane do Twojej firmy</li>
          <li>Jeden zaufany punkt kontaktu dla IT, Microsoft 365 i danych</li>
          <li>Lokalne korzenie, ze wsparciem zdalnym tam, gdzie ma to sens</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container about-layout">
    <div>
      <span class="kicker">Gdzie pracujemy</span>
      <h2>Lokalne wsparcie w Northamptonshire, zdalne wsparcie dalej</h2>
      <p>Cevano współpracuje z firmami na miejscu w okolicach Northampton, Kettering, Milton Keynes, Rugby oraz na terenach Northamptonshire, Warwickshire i Buckinghamshire. Tam, gdzie wizyta nie jest konieczna, chętnie pomożemy również zdalnie — wiele zadań związanych z Microsoft 365 i analizą danych da się zrealizować równie skutecznie w ten sposób.</p>
      <div class="area-tags">
        <span>Northampton</span><span>Kettering</span><span>Milton Keynes</span><span>Rugby</span>
        <span>Northamptonshire</span><span>Warwickshire</span><span>Buckinghamshire</span><span>Zdalnie w całej Wielkiej Brytanii</span>
      </div>
    </div>
    <div class="about-graphic">{ABOUT_LOCATION_GRAPHIC}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h2>Chcesz sprawdzić, czy dobrze pasujemy do Twojej firmy?</h2>
        <p>Skontaktuj się z nami i opowiedz, czego potrzebujesz.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Skontaktuj się</a>
    </div>
  </div>
</section>
'''

write("pl/about.html", page(
    "pl", "", "../", "about",
    "O Cevano IT Solutions | Praktyczne IT dla małych firm",
    "Cevano IT Solutions zapewnia praktyczne wsparcie IT, zarządzanie Microsoft 365 oraz analizę danych dla małych firm w Northamptonshire.",
    "about.html", "about.html", body_about_pl, alt_href="../about.html"
))
