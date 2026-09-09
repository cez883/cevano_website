# -*- coding: utf-8 -*-
from build import *

# ================================================================
# CONTACT — EN
# ================================================================
body_contact_en = '''
<section class="page-hero">
  <div class="container">
    <h1>How can we help?</h1>
    <p>Tell us what you need help with and we'll get back to you.</p>
  </div>
</section>

<section class="section">
  <div class="container contact-layout">
    <div class="contact-info">
      <div class="info-block">
        <h3>Email</h3>
        <a class="email-link" href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a>
        <p>The quickest way to reach us — describe what you need and we'll reply as soon as we can.</p>
      </div>
      <div class="info-block">
        <h3>Where we work</h3>
        <p>On-site around Northampton, Kettering, Milton Keynes, Rugby and the surrounding areas — remote support available further afield.</p>
        <div class="area-tags">
          <span>Northampton</span><span>Kettering</span><span>Milton Keynes</span><span>Rugby</span><span>Remote UK-wide</span>
        </div>
      </div>
      <div class="info-block">
        <h3>What to include</h3>
        <p>A short description of the problem or project, roughly how many people or devices are involved, and whether it's urgent — that's usually enough for us to point you in the right direction.</p>
      </div>
    </div>

    <div class="form-card">
      <form data-contact-form action="/api/contact" method="post"
            data-success-msg="Thank you. Your enquiry has been sent successfully. We'll be in touch as soon as possible."
            data-error-msg="Sorry, something went wrong sending your message. Please email us directly at enquiries@cevano.co.uk instead."
            data-submit-label="Send enquiry" data-sending="Sending…">
        <input type="hidden" name="_lang" value="en">
        <div class="hp-field" aria-hidden="true">
          <label for="company_website">Leave this field empty</label>
          <input type="text" id="company_website" name="company_website" tabindex="-1" autocomplete="off">
        </div>

        <div class="form-row">
          <label for="name">Name <span class="req">*</span></label>
          <input type="text" id="name" name="name" required autocomplete="name">
        </div>

        <div class="form-two">
          <div class="form-row">
            <label for="company">Company name</label>
            <input type="text" id="company" name="company" autocomplete="organization">
          </div>
          <div class="form-row">
            <label for="phone">Phone</label>
            <input type="tel" id="phone" name="phone" autocomplete="tel">
          </div>
        </div>

        <div class="form-two">
          <div class="form-row">
            <label for="email">Email <span class="req">*</span></label>
            <input type="email" id="email" name="email" required autocomplete="email">
          </div>
          <div class="form-row">
            <label for="service">Service / area of support</label>
            <select id="service" name="service">
              <option value="">Not sure / general enquiry</option>
              <option value="IT Support">IT Support</option>
              <option value="Microsoft 365">Microsoft 365</option>
              <option value="Data Analytics / Power BI">Data Analytics / Power BI</option>
              <option value="Networking & AV">Networking &amp; AV</option>
              <option value="IT Assets & Documentation">IT Assets &amp; Documentation</option>
              <option value="Domains & Online Services">Domains &amp; Online Services</option>
              <option value="Other">Other</option>
            </select>
          </div>
        </div>

        <div class="form-row">
          <label for="message">Message <span class="req">*</span></label>
          <textarea id="message" name="message" required placeholder="Tell us what you need help with. For example, IT support, Microsoft 365, a new office setup, Power BI reporting or another technology requirement."></textarea>
        </div>

        <div class="form-row">
          <label style="display:flex; gap:10px; font-weight:400; align-items:flex-start; cursor:pointer;">
            <input type="checkbox" required name="consent" style="width:auto; margin-top:4px;">
            <span style="font-size:14px; color:var(--slate);">I agree to Cevano IT Solutions storing and using my details to respond to my enquiry, in line with the <a href="legal/privacy-policy.html" style="color:var(--blue-mid); font-weight:600;">Privacy Policy</a>. <span class="req">*</span></span>
          </label>
        </div>

        <button type="submit" class="btn btn-primary" data-form-submit style="width:100%;">Send enquiry</button>
        <p class="form-note">We only use your details to respond to your enquiry. See our <a href="legal/privacy-policy.html">Privacy Policy</a> for more information.</p>
        <div class="form-status" data-form-status aria-live="polite"></div>
      </form>
    </div>
  </div>
</section>
'''

write("contact.html", page(
    "en", "", "", "contact",
    "Contact Cevano IT Solutions | Get in Touch",
    "Get in touch with Cevano IT Solutions for IT support, Microsoft 365 or data analytics — serving Northampton, Kettering, Milton Keynes, Rugby and remote clients UK-wide.",
    "contact.html", "contact.html", body_contact_en, alt_href="pl/contact.html"
))

# ================================================================
# CONTACT — PL
# ================================================================
body_contact_pl = '''
<section class="page-hero">
  <div class="container">
    <h1>W czym możemy pomóc?</h1>
    <p>Napisz, z czym potrzebujesz pomocy, a odezwiemy się do Ciebie.</p>
  </div>
</section>

<section class="section">
  <div class="container contact-layout">
    <div class="contact-info">
      <div class="info-block">
        <h3>E-mail</h3>
        <a class="email-link" href="mailto:enquiries@cevano.co.uk">enquiries@cevano.co.uk</a>
        <p>Najszybszy sposób, aby się z nami skontaktować — opisz, czego potrzebujesz, a odpowiemy najszybciej jak to możliwe.</p>
      </div>
      <div class="info-block">
        <h3>Gdzie pracujemy</h3>
        <p>Na miejscu w okolicach Northampton, Kettering, Milton Keynes, Rugby i okolic — wsparcie zdalne dostępne również dalej.</p>
        <div class="area-tags">
          <span>Northampton</span><span>Kettering</span><span>Milton Keynes</span><span>Rugby</span><span>Zdalnie w całej UK</span>
        </div>
      </div>
      <div class="info-block">
        <h3>Co warto podać</h3>
        <p>Krótki opis problemu lub projektu, orientacyjną liczbę osób lub urządzeń, których to dotyczy, oraz czy sprawa jest pilna — zwykle to wystarczy, abyśmy mogli wskazać właściwy kierunek.</p>
      </div>
    </div>

    <div class="form-card">
      <form data-contact-form action="/api/contact" method="post"
            data-success-msg="Dziękujemy. Twoje zapytanie zostało wysłane. Odezwiemy się najszybciej jak to możliwe."
            data-error-msg="Niestety wystąpił problem podczas wysyłania wiadomości. Napisz do nas bezpośrednio na enquiries@cevano.co.uk."
            data-submit-label="Wyślij zapytanie" data-sending="Wysyłanie…">
        <input type="hidden" name="_lang" value="pl">
        <div class="hp-field" aria-hidden="true">
          <label for="company_website_pl">Pozostaw to pole puste</label>
          <input type="text" id="company_website_pl" name="company_website" tabindex="-1" autocomplete="off">
        </div>

        <div class="form-row">
          <label for="name_pl">Imię i nazwisko <span class="req">*</span></label>
          <input type="text" id="name_pl" name="name" required autocomplete="name">
        </div>

        <div class="form-two">
          <div class="form-row">
            <label for="company_pl">Nazwa firmy</label>
            <input type="text" id="company_pl" name="company" autocomplete="organization">
          </div>
          <div class="form-row">
            <label for="phone_pl">Telefon</label>
            <input type="tel" id="phone_pl" name="phone" autocomplete="tel">
          </div>
        </div>

        <div class="form-two">
          <div class="form-row">
            <label for="email_pl">E-mail <span class="req">*</span></label>
            <input type="email" id="email_pl" name="email" required autocomplete="email">
          </div>
          <div class="form-row">
            <label for="service_pl">Usługa / obszar wsparcia</label>
            <select id="service_pl" name="service">
              <option value="">Nie jestem pewien / zapytanie ogólne</option>
              <option value="IT Support">Wsparcie IT</option>
              <option value="Microsoft 365">Microsoft 365</option>
              <option value="Data Analytics / Power BI">Analiza danych / Power BI</option>
              <option value="Networking & AV">Sieci i AV</option>
              <option value="IT Assets & Documentation">Zasoby IT i dokumentacja</option>
              <option value="Domains & Online Services">Domeny i usługi online</option>
              <option value="Other">Inne</option>
            </select>
          </div>
        </div>

        <div class="form-row">
          <label for="message_pl">Wiadomość <span class="req">*</span></label>
          <textarea id="message_pl" name="message" required placeholder="Napisz, z czym potrzebujesz pomocy. Na przykład wsparcie IT, Microsoft 365, organizacja nowego biura, raportowanie Power BI lub inna potrzeba technologiczna."></textarea>
        </div>

        <div class="form-row">
          <label style="display:flex; gap:10px; font-weight:400; align-items:flex-start; cursor:pointer;">
            <input type="checkbox" required name="consent" style="width:auto; margin-top:4px;">
            <span style="font-size:14px; color:var(--slate);">Wyrażam zgodę na przechowywanie i wykorzystanie moich danych przez Cevano IT Solutions w celu odpowiedzi na moje zapytanie, zgodnie z <a href="legal/privacy-policy.html" style="color:var(--blue-mid); font-weight:600;">Polityką prywatności</a>. <span class="req">*</span></span>
          </label>
        </div>

        <button type="submit" class="btn btn-primary" data-form-submit style="width:100%;">Wyślij zapytanie</button>
        <p class="form-note">Twoje dane wykorzystujemy wyłącznie w celu odpowiedzi na zapytanie. Więcej informacji znajdziesz w <a href="legal/privacy-policy.html">Polityce prywatności</a>.</p>
        <div class="form-status" data-form-status aria-live="polite"></div>
      </form>
    </div>
  </div>
</section>
'''

write("pl/contact.html", page(
    "pl", "", "../", "contact",
    "Kontakt z Cevano IT Solutions | Skontaktuj się",
    "Skontaktuj się z Cevano IT Solutions w sprawie wsparcia IT, Microsoft 365 lub analizy danych — obsługujemy Northampton, Kettering, Milton Keynes, Rugby oraz klientów zdalnych w całej UK.",
    "contact.html", "contact.html", body_contact_pl, alt_href="../contact.html"
))
