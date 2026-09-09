# Cevano IT Solutions — Przewodnik wdrożenia

**Architektura: GitHub → Cloudflare Pages → cevano.co.uk, z DNS na Cloudflare,
Resend obsługującym formularz kontaktowy oraz Microsoft 365 jako jedynym
dostawcą poczty.**

To jest kompletnie nowa wersja przewodnika wdrożenia, powstała po migracji
z hostingu współdzielonego Hostinger/PHP na architekturę statyczną i
bezserwerową (serverless). Jeśli szukasz starych instrukcji dla Hostinger —
już nie obowiązują, ten dokument całkowicie je zastępuje.

---

## 1. Przegląd projektu

To jest produkcyjna strona internetowa Cevano IT Solutions: statyczna strona
HTML/CSS/JS (wersja angielska i polska) z jedną niewielką funkcją
bezserwerową obsługującą formularz kontaktowy. Nie ma tu bazy danych, CMS-a,
kroku budowania (build), a od tej migracji — również PHP i tradycyjnego
serwera WWW.

```
cevano-site/
├── index.html, services.html, about.html, contact.html, 404.html   ← strony angielskie
├── pl/                                                              ← strony polskie (odzwierciedlają powyższe)
│   ├── index.html, services.html, about.html, contact.html
│   └── legal/privacy-policy.html, legal/terms.html
├── legal/
│   ├── privacy-policy.html
│   └── terms.html
├── css/style.css                 ← cały styl (motyw jasny + ciemny)
├── js/main.js                    ← przełącznik motywu, menu mobilne, banner cookies,
│                                    formularz kontaktowy, animacje scroll, mini-nav
├── assets/img/                   ← logo, favicony, obraz do udostępniania w social media
├── functions/
│   └── api/
│       └── contact.js            ← Cloudflare Pages Function (formularz kontaktowy)
├── _headers                      ← nagłówki bezpieczeństwa/cache dla Cloudflare Pages
├── _redirects                    ← reguły przekierowań Cloudflare Pages (kanoniczne www)
├── robots.txt
├── sitemap.xml
├── site.webmanifest
├── .gitignore
└── build*.py, build.py           ← skrypty Pythona generujące HTML
                                     (wyłącznie narzędzie deweloperskie — patrz §14)
```

---

## 2. Finalna architektura

```
                 ┌──────────────────────┐
  Praca lokalna →│  GitHub (prywatne)    │
                 └──────────┬───────────┘
                             │ git push do main
                             ▼
                 ┌──────────────────────┐
                 │  Cloudflare Pages    │  ← automatyczne wdrożenie po każdym pushu
                 │  (hosting statyczny) │
                 └──────────┬───────────┘
                             │
                             ▼
GoDaddy (rejestrator) ──DNS──▶ Cloudflare DNS ──▶ https://www.cevano.co.uk

Formularz kontaktowy:

  contact.html / pl/contact.html
          │  fetch() POST
          ▼
  functions/api/contact.js   (Cloudflare Pages Function)
          │  wywołanie REST API, sekret po stronie serwera
          ▼
  Resend (transakcyjne API e-mail)
          │  wysyła e-mail
          ▼
  enquiries@cevano.co.uk
          │
          ▼
  Microsoft 365 / Exchange Online  ← tu faktycznie znajduje się skrzynka
```

**Co się zmieniło względem starej konfiguracji Hostinger:**

| Przed (Hostinger) | Teraz (Cloudflare) |
|---|---|
| Apache + `.htaccess` | Sieć brzegowa Cloudflare + `_headers` / `_redirects` |
| PHP `contact-handler.php` + `mail()` | `functions/api/contact.js` (Pages Function) + Resend API |
| Wgrywanie przez FTP/File Manager | `git push` → automatyczne wdrożenie |
| SPF/DKIM skonfigurowane *dla poczty Hostinger* | Niepotrzebne — poczta Hostinger całkowicie zniknęła |
| Ręczny DNS w GoDaddy | DNS zarządzany w Cloudflare (GoDaddy pozostaje rejestratorem) |

**Co NIE się zmieniło:** wygląd wizualny, treść stron, wersje
angielska/polska, wszystkie adresy URL (wciąż ścieżki `.html`, np.
`/services.html`), metadane SEO oraz Microsoft 365 jako Twój dostawca
poczty — nic dotyczące `enquiries@cevano.co.uk` ani jego rekordów DNS nie
jest dotknięte tą migracją.

---

## 3. Konfiguracja GitHub

1. Utwórz **prywatne** repozytorium GitHub (np. `cevano-website`).
2. Z poziomu folderu projektu zainicjuj i wypchnij kod:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Cevano IT Solutions website"
   git branch -M main
   git remote add origin https://github.com/<twoja-nazwa>/cevano-website.git
   git push -u origin main
   ```
3. Sprawdź, czy `.gitignore` (dołączony) działa poprawnie — uruchom
   `git status` przed pierwszym commitem i upewnij się, że żaden plik typu
   `.dev.vars` czy `.env` nie jest wśród plików do zatwierdzenia. **Żadne
   klucze API ani sekrety nigdy nie powinny trafić do repozytorium.**

Od tego momentu gałąź `main` na GitHubie jest źródłem prawdy: każdy push do
`main` automatycznie uruchamia nowe wdrożenie Cloudflare Pages (§13).

---

## 4. Konfiguracja konta Cloudflare

1. Załóż darmowe konto na cloudflare.com, jeśli jeszcze go nie masz (wiele
   osób korzysta z Cloudflare wyłącznie do DNS — jeśli tak jest w Twoim
   przypadku, możesz użyć tego samego konta).
2. Będziesz potrzebować dwóch rzeczy skonfigurowanych na tym koncie przed
   wdrożeniem:
   - Projektu **Cloudflare Pages** (§5)
   - **Cloudflare DNS** dla cevano.co.uk (§9)

---

## 5. Wdrożenie na Cloudflare Pages

1. W panelu Cloudflare przejdź do **Workers & Pages → Create → Pages →
   Connect to Git**.
2. Wybierz swoje repozytorium GitHub `cevano-website` (zostaniesz poproszony
   o autoryzację aplikacji GitHub od Cloudflare — jeśli masz taką opcję,
   ogranicz dostęp tylko do tego jednego repozytorium).
3. Skonfiguruj ustawienia budowania dokładnie tak:

   | Ustawienie | Wartość |
   |---|---|
   | Framework preset | **None** |
   | Build command | *(pozostaw puste)* |
   | Build output directory | `/` (katalog główny repozytorium) |
   | Root directory | `/` (chyba że strona jest zagnieżdżona w podfolderze) |

   To zwykła strona statyczna bez kroku budowania — Cloudflare wdraża
   zawartość repozytorium bez zmian i automatycznie rozpoznaje `_headers`,
   `_redirects` oraz folder `functions/`.
4. Kliknij **Save and Deploy**. Pierwsze wdrożenie uruchomi się natychmiast
   i otrzymasz tymczasowy adres w stylu `cevano-website.pages.dev` — użyj
   go do przetestowania wszystkiego (§12) przed podłączeniem docelowej
   domeny.

---

## 6. Zmienne środowiskowe i sekrety

Ustaw je w **Cloudflare Pages → Twój projekt → Settings → Environment
variables**, dla środowiska **Production** (a także Preview, jeśli chcesz,
aby formularz kontaktowy działał również na wdrożeniach podglądowych).

| Nazwa | Typ | Wymagane | Wartość |
|---|---|---|---|
| `RESEND_API_KEY` | **Sekret** | Tak | Twój klucz API Resend (§7) |
| `TO_EMAIL` | Tekst jawny | Nie | Domyślnie `enquiries@cevano.co.uk` — ustaw tylko, jeśli zapytania mają trafiać gdzie indziej |
| `FROM_EMAIL` | Tekst jawny | Nie | `"Cevano Website <forms@notifications.cevano.co.uk>"` po zweryfikowaniu subdomeny wysyłkowej w Resend (§7). Domyślnie używana jest współdzielona domena testowa Resend, jeśli nie ustawiono. |
| `TURNSTILE_SECRET_KEY` | **Sekret** | Nie | Tylko jeśli włączysz Cloudflare Turnstile (§16) |

**Nigdy** nie umieszczaj tych wartości bezpośrednio w kodzie ani nie
zatwierdzaj ich w GitHubie — zawsze korzystaj z interfejsu zmiennych
środowiskowych Cloudflare (lub `wrangler pages secret put <NAZWA>`, jeśli
używasz CLI). Oznacz `RESEND_API_KEY` i `TURNSTILE_SECRET_KEY` jako
**Secret** (nie plain text), aby były zaszyfrowane i nigdy więcej nie
wyświetlane w panelu po zapisaniu.

Po dodaniu lub zmianie zmiennych środowiskowych konieczne jest
**ponowne wdrożenie** (Cloudflare Pages → Deployments → retry latest, albo
po prostu nowy push), aby funkcja je uwzględniła.

---

## 7. Dostawca poczty transakcyjnej: Resend

**Dlaczego Resend:** hojny darmowy plan (3000 e-maili/miesiąc, 100/dzień —
w zupełności wystarczające dla formularza kontaktowego małej firmy), prosty
REST API niewymagający SDK ani zależności npm (funkcja korzysta wyłącznie z
`fetch()`), solidna dostarczalność oraz jeden z najczęściej rekomendowanych
dostawców właśnie do tego zastosowania z Cloudflare Pages Functions. Jest
też całkowicie niezależny od Microsoft 365 — po prostu wysyła wiadomość *do*
Twojej skrzynki M365, tak jak zrobiłby to każdy zewnętrzny nadawca.

**Konfiguracja:**

1. Załóż darmowe konto na resend.com.
2. Przejdź do **API Keys → Create API Key**, nazwij go np.
   `cevano-website-contact-form` i ogranicz uprawnienia wyłącznie do
   **Sending access** (nie pełny dostęp do konta). Skopiuj klucz od razu —
   nie zobaczysz go ponownie.
3. Dodaj go jako sekret `RESEND_API_KEY` w Cloudflare Pages (§6).

**Domena wysyłkowa — dwie opcje:**

- **Szybki start (tylko do testów):** pozostaw `FROM_EMAIL` nieustawione.
  Funkcja domyślnie użyje współdzielonej domeny Resend
  (`onboarding@resend.dev`), która działa od razu, bez żadnej konfiguracji
  DNS — wystarczające do potwierdzenia, że wszystko działa od początku do
  końca, ale nieidealne produkcyjnie (ogólny adres nadawcy, słabsza
  reputacja dostarczalności).
- **Zalecane produkcyjnie:** zweryfikuj w Resend **subdomenę**, którą
  kontrolujesz, np. `notifications.cevano.co.uk`. W Resend przejdź do
  **Domains → Add Domain**, wpisz `notifications.cevano.co.uk` (nie samą
  `cevano.co.uk`), a Resend poda Ci niewielki zestaw rekordów DNS
  (SPF/TXT, DKIM/CNAME) do dodania.

  **To jest kluczowa część dla Ciebie:** ponieważ te rekordy dotyczą
  subdomeny `notifications.`, są całkowicie oddzielone od istniejących
  rekordów SPF/DKIM/MX Microsoft 365 na domenie głównej — brak
  jakiegokolwiek nakładania się czy konieczności łączenia. Pełne
  szczegóły w §10.

  Po weryfikacji ustaw `FROM_EMAIL` na coś w stylu:
  `"Cevano Website <forms@notifications.cevano.co.uk>"`

---

## 8. Podłączenie własnej domeny

Gdy DNS jest już na Cloudflare (§9), a pierwsze wdrożenie Pages działa:

1. W **Cloudflare Pages → Twój projekt → Custom domains → Set up a custom
   domain** dodaj `www.cevano.co.uk` (wersja kanoniczna używana w
   metadanych SEO całej strony — patrz uwaga w pliku `_redirects`).
2. Dodaj również samą domenę `cevano.co.uk` (bez www) jako drugą domenę
   niestandardową.
3. Cloudflare automatycznie utworzy odpowiednie rekordy DNS dla obu (skoro
   DNS jest już na Cloudflare, to jednoklikowy krok, a nie ręczne wpisywanie
   rekordów).
4. Dołączony w projekcie plik `_redirects` już przekierowuje 301
   `cevano.co.uk` → `www.cevano.co.uk`, więc obie wersje działają, ale
   tylko jedna jest kanoniczna dla wyszukiwarek.

---

## 9. Przeniesienie DNS z GoDaddy do Cloudflare

Domena **pozostaje zarejestrowana w GoDaddy** — przenosisz jedynie
*zarządzanie* DNS do Cloudflare, nie samą rejestrację.

1. W Cloudflare przejdź do **Add a Site**, wpisz `cevano.co.uk` i wybierz
   plan darmowy.
2. Cloudflare przeskanuje istniejące rekordy DNS Twojej domeny i pokaże
   listę — **dokładnie przejrzyj tę listę, zanim przejdziesz dalej** (patrz
   §10, co dokładnie sprawdzić).
3. Cloudflare poda Ci dwa serwery nazw (nameservers), np.
   `ns1.cloudflare.com` / `ns2.cloudflare.com` (Twoje będą specyficzne dla
   konta).
4. Zaloguj się do **GoDaddy → My Products → Domains → DNS** dla
   cevano.co.uk i zmień serwery nazw z domyślnych GoDaddy na dwa serwery
   Cloudflare.
5. Zapisz. Propagacja zwykle trwa od kilku minut do 24 godzin. Cloudflare
   wyśle e-mail, gdy wykryje zmianę.

⚠️ **Rób to świadomie, nie na szybko** — dopóki nie zakończysz listy
kontrolnej z §10, nie usuwaj ani nie "porządkuj" żadnych istniejących
rekordów DNS zaimportowanych przez Cloudflare. Zbędne/nieużywane rekordy
można usunąć później; brakujący rekord MX lub SPF może natychmiast zepsuć
pocztę.

---

## 10. Zachowanie poczty Microsoft 365 — kluczowa lista kontrolna

To krok najbardziej narażony na realne szkody, jeśli zostanie wykonany w
pośpiechu, więc traktuj go jako osobną listę kontrolną, niezależną od
ogólnego przenoszenia DNS powyżej.

**Przed zmianą serwerów nazw** zaloguj się do centrum administracyjnego
Microsoft 365 → **Settings → Domains → cevano.co.uk → DNS records** i
zanotuj każdy widoczny tam rekord. Zazwyczaj wygląda to mniej więcej tak:

| Typ | Cel | Przykład (Twój będzie inny) |
|---|---|---|
| MX | Kieruje przychodzącą pocztę do Exchange Online | `cevano-co-uk.mail.protection.outlook.com` |
| TXT (SPF) | Autoryzuje Microsoft 365 do wysyłania w imieniu Twojej domeny | `v=spf1 include:spf.protection.outlook.com -all` |
| CNAME × 2 | Klucze podpisywania DKIM | `selector1._domainkey`, `selector2._domainkey` |
| CNAME | Autodiscover (do konfiguracji klienta Outlook) | `autodiscover.cevano.co.uk` |
| TXT (opcjonalnie) | Polityka DMARC, jeśli skonfigurowana | `_dmarc.cevano.co.uk` |

**Po zaimportowaniu rekordów DNS przez Cloudflare** (krok 2 w §9),
zweryfikuj, że każdy z powyższych jest obecny i niezmieniony w panelu DNS
Cloudflare. Skanowanie importu Cloudflare jest zazwyczaj wiarygodne, ale
ręcznie porównaj je z listą z centrum administracyjnego Microsoft 365 —
nie zakładaj, że wszystko się zgadza.

**Dodanie rekordów Resend (§7) NIE spowoduje konfliktu**, ponieważ:
- Rekordy Resend znajdują się na subdomenie (`notifications.cevano.co.uk`),
  nie na domenie głównej — to całkowicie osobna przestrzeń DNS względem
  rekordów SPF/DKIM M365 na domenie głównej.
- Gdybyś kiedykolwiek potrzebował rekordu SPF na dokładnie tej samej nazwie
  hosta co istniejący, SPF wymaga połączenia w jeden rekord (kilka
  rekordów TXT SPF na tej samej nazwie hosta psuje weryfikację SPF) — ale
  ponieważ podejście z subdomeną Resend całkowicie tego unika, w tej
  konfiguracji nie ma nic do łączenia.

**Jeszcze jedna rzecz do sprawdzenia:** proxy Cloudflare (ikona pomarańczowej
chmurki) dotyczy tylko rekordów A/AAAA/CNAME dla ruchu *WWW* — dla rekordów
MX i wszelkich rekordów CNAME/TXT związanych z pocztą powinno być ustawione
na **DNS only (szara chmurka)**, ponieważ proxy nie ma zastosowania do
routingu poczty. Cloudflare domyślnie ustawia rekordy MX jako DNS-only
automatycznie, ale warto to szybko wizualnie sprawdzić.

**Ostateczna weryfikacja po propagacji zmiany serwerów nazw:** wyślij testowy
e-mail na `enquiries@cevano.co.uk` z zewnętrznego adresu (np. Gmail) i
potwierdź, że dociera normalnie do Outlook/Exchange Online, tak jak wcześniej.

---

## 11. Konfiguracja SSL

Cloudflare Pages automatycznie wystawia i odnawia certyfikaty SSL zarówno
dla adresu `.pages.dev`, jak i dla wszystkich podłączonych domen
niestandardowych — nic nie trzeba ręcznie konfigurować. W
**Cloudflare → SSL/TLS** zalecany tryb dla projektu Pages to
**Full (strict)**, zwykle domyślny. Przekierowania HTTPS są automatyczne;
reguła "wymuś HTTPS", która wcześniej znajdowała się w `.htaccess`, nie
jest już potrzebna.

---

## 12. Testowanie formularza kontaktowego

Testuj najpierw na tymczasowym adresie `*.pages.dev`, a potem ponownie na
domenie docelowej po jej podłączeniu.

1. **Formularz angielski** (`/contact.html`): wyślij zgłoszenie z prawdziwym
   adresem e-mail, który możesz sprawdzić, wypełniając wszystkie pola.
   Potwierdź, że:
   - Komunikat o sukcesie pojawia się w treści strony (bez przeładowania)
   - E-mail dociera na `enquiries@cevano.co.uk` w Outlooku
   - **Reply-To** jest ustawione na adres, który podałeś (kliknij "odpowiedz"
     i sprawdź)
   - Treść e-maila zawiera imię i nazwisko, firmę, e-mail, telefon, usługę,
     język (EN) oraz wiadomość
2. **Formularz polski** (`/pl/contact.html`): powtórz powyższe, potwierdź, że
   w e-mailu pojawia się `Language: PL`, a komunikaty sukcesu/błędu na
   stronie są po polsku.
3. **Walidacja:** spróbuj wysłać formularz z pustym wymaganym polem,
   nieprawidłowym e-mailem oraz bez zaznaczenia zgody — potwierdź, że każdy
   przypadek pokazuje błąd w treści strony bez wysyłania e-maila.
4. **Honeypot:** trudny do przetestowania ręcznie z założenia, ale możesz
   potwierdzić istnienie ukrytego pola, przeglądając kod źródłowy strony i
   szukając `name="company_website"` wewnątrz formularza.
5. **Fallback bez JS (opcjonalnie, ale warto sprawdzić raz):** wyłącz
   JavaScript w przeglądarce, wyślij formularz i potwierdź, że zostajesz
   przekierowany z powrotem na stronę kontaktową z widocznym komunikatem
   potwierdzającym (przez parametr `?sent=1`).

---

## 13. Przepływ wdrożenia

Po podłączeniu, to jest cały codzienny przepływ pracy:

```
Edycja plików lokalnie
      ↓
git add . && git commit -m "..."
      ↓
git push origin main
      ↓
Cloudflare Pages automatycznie wykrywa push
      ↓
Buduje i wdraża w ciągu ~1 minuty
      ↓
Strona live na www.cevano.co.uk
```

Nigdy żadnego ręcznego wgrywania plików. Każdy push do `main` to wdrożenie
produkcyjne. Jeśli chcesz mieć etap podglądu/recenzji przed publikacją,
wypchnij najpierw do innej gałęzi i otwórz pull request — Cloudflare Pages
automatycznie buduje **adres podglądowy** dla każdej gałęzi/PR-a, dzięki
czemu możesz sprawdzić zmiany przed scaleniem do `main`.

---

## 14. Skrypty budujące Pythona (`build.py` / `build_*.py`)

**Rekomendacja: zachować.** Te skrypty generują strony HTML na podstawie
współdzielonych szablonów (nagłówek, stopka, nawigacja, przełącznik języka),
dzięki czemu zmiana ogólnostronicowa — aktualizacja stopki, dodanie linku do
nawigacji, edycja adresu firmy — dzieje się raz w `build.py` i konsekwentnie
regeneruje wszystkie 16 stron, zamiast ręcznej edycji każdej strony
angielskiej i polskiej osobno (gdzie na dwujęzycznych stronach łatwo o
pomyłki, co kilkukrotnie zdarzyło się podczas wcześniejszego rozwoju tego
projektu).

**Są to wyłącznie narzędzia deweloperskie** — Cloudflare Pages nie uruchamia
Pythona, nie wie o istnieniu tych plików i nie potrzebuje ich podczas
wdrożenia. Wdraża wyłącznie statyczne pliki HTML/CSS/JS/Function już
znajdujące się w repozytorium. Ustawienie "Build command" w Cloudflare Pages
(§5, pozostawione puste) w żaden sposób ich nie wywołuje.

**Aby wprowadzić zmianę ogólnostronicową:**
```bash
# edytuj build.py lub odpowiedni plik build_*.py, następnie:
python3 build_home.py
python3 build_services.py
python3 build_about.py
python3 build_contact.py
python3 build_legal.py
python3 build_404.py
# następnie zatwierdź i wypchnij zregenerowane pliki HTML jak zwykle
```

Gdybyś w przyszłości wolał nie utrzymywać zestawu narzędzi Pythona, naturalnym
kolejnym krokiem byłby system szablonów wbudowany w generator stron
statycznych (Eleventy, Astro itp.) — ale biorąc pod uwagę obecny rozmiar
strony (16 stron, brak planów gwałtownego wzrostu), istniejące skrypty są
proste, bezzależnościowe i łatwe do przeczytania od początku do końca w
kilka minut przez każdego przyszłego dewelopera, więc migracja nie jest
obecnie konieczna.

---

## 15. Przegląd prywatności / RODO

Polityka prywatności i cookies (`/legal/privacy-policy.html` oraz
`/pl/legal/privacy-policy.html`) została zaktualizowana, aby odzwierciedlić
nową architekturę:

- **Cloudflare** jest teraz wymieniony jako dostawca hostingu/infrastruktury
- **Resend** jest teraz wymieniony jako podmiot przetwarzający pocztę
  transakcyjną dla formularza kontaktowego
- **Microsoft 365 / Exchange Online** jest wymieniony jako miejsce, gdzie
  faktycznie znajduje się skrzynka `enquiries@cevano.co.uk`
- **Usunięto zbieranie adresów IP** z samego e-maila formularza
  kontaktowego — stary handler PHP zawierał adres IP nadawcy w e-mailu z
  powiadomieniem; nowa funkcja Cloudflare tego nie robi, ponieważ nie było
  to nigdzie wykorzystywane, a minimalizacja zbieranych danych to lepsza
  praktyka. Polityka teraz dokładnie wskazuje, że Cloudflare jako
  infrastruktura przetwarza standardowe dane połączenia w ramach normalnego
  działania sieci, ale samo Cevano ich osobno nie zbiera ani nie
  przechowuje.

**Pozostałe placeholdery, które musisz jeszcze uzupełnić** (oznaczone żółtą
etykietą "Placeholder" na obu stronach prawnych):

- Data ostatniej publikacji/aktualizacji Polityki prywatności i Regulaminu
- Numer VAT, jeśli dotyczy (numer firmy i adres siedziby są już uzupełnione
  podanymi przez Ciebie danymi)
- Potwierdzenie, czy używane jest jakiekolwiek narzędzie analityczne —
  sekcja Cookies obecnie oznacza to jako niepotwierdzone; jeśli nie
  korzystasz z żadnej analityki, można to po prostu zmienić na odpowiednią
  informację

Żadne inne zbieranie danych nie zostało wymyślone ani założone — polityka
opisuje wyłącznie to, co strona i formularz kontaktowy faktycznie robią.

---

## 16. Podsumowanie przeglądu bezpieczeństwa

Podstawowy przegląd odpowiedni dla strony małej firmy, bez nadmiernego
komplikowania rozwiązania:

- **Walidacja danych wejściowych:** wszystkie pola formularza kontaktowego
  są walidowane po stronie serwera w `functions/api/contact.js` (pola
  wymagane, format e-mail, zgoda) — nigdy nie polegając wyłącznie na
  walidacji po stronie klienta.
- **Ochrona przed spamem:** pole honeypot + mechanizm czasowy po stronie
  klienta (odrzuca zgłoszenia wysłane szybciej niż w 2,5 sekundy) są
  aktywne domyślnie, bez potrzeby konfiguracji. **Cloudflare Turnstile**
  jest obsługiwany i zalecany jako dodatkowa warstwa, jeśli spam stanie się
  problemem — wyjaśnienie poniżej, dlaczego nie jest włączony domyślnie na
  siłę.
- **Sekrety:** `RESEND_API_KEY` oraz (jeśli używany) `TURNSTILE_SECRET_KEY`
  są przechowywane jako zaszyfrowane sekrety Cloudflare, nigdy w kodzie ani
  w GitHubie. Funkcja działa po stronie serwera, więc klucz API nigdy nie
  jest widoczny w przeglądarce.
- **Nagłówki bezpieczeństwa:** `_headers` ustawia `X-Content-Type-Options`,
  `X-Frame-Options`, `Referrer-Policy` oraz zachowawczy `Permissions-Policy`
  na każdej trasie.
- **HTTPS:** wymuszany automatycznie przez Cloudflare na każdej trasie, bez
  konieczności konfiguracji.
- **CORS:** nie dotyczy — formularz kontaktowy wywołuje wyłącznie
  `/api/contact` w ramach tego samego źródła (adres względny), więc nie ma
  żądania cross-origin do skonfigurowania czy ograniczenia.
- **Ograniczanie liczby żądań (rate limiting):** nie skonfigurowane osobno.
  Ochrona przed DDoS na poziomie platformy Cloudflare stosuje się
  automatycznie do każdego projektu Pages; w połączeniu z honeypotem/
  mechanizmem czasowym (oraz opcjonalnym Turnstile) stanowi to adekwatny
  poziom ochrony dla formularza kontaktowego małej firmy. Jeśli w
  przyszłości wolumen spamu stanie się realnym problemem, reguły rate
  limiting Cloudflare (dostępne w ograniczonej formie nawet w planie
  darmowym) są naturalnym kolejnym krokiem.

### Czy warto włączyć Cloudflare Turnstile?

**Rekomendacja: warto dodać, jeśli/gdy spam stanie się realnym problemem —
nie jest wymagane do uruchomienia strony.** Połączenie honeypota i
mechanizmu czasowego wyłapuje zdecydowaną większość zautomatyzowanych
botów spamowych bez żadnego tarcia dla prawdziwych odwiedzających.
Turnstile dodaje znacząco silniejszą ochronę przed bardziej
zaawansowanymi botami, a skoro i tak korzystasz z Cloudflare, jest darmowy
i dobrze zintegrowany. Kompromis to jeden dodatkowy element systemu i
niewielki widoczny element w formularzu.

`functions/api/contact.js` ma już wbudowaną pełną obsługę — jeśli
`TURNSTILE_SECRET_KEY` jest ustawiony, weryfikacja jest wymuszana; jeśli
pozostawiony pusty, Turnstile jest całkowicie pomijany, a formularz działa
dokładnie tak, jak został dostarczony.

**Aby włączyć go później:**
1. W panelu Cloudflare → **Turnstile → Add site**, zarejestruj
   `cevano.co.uk`, wybierz typ widgetu "Managed" i skopiuj **Site Key** oraz
   **Secret Key**.
2. Ustaw `TURNSTILE_SECRET_KEY` jako sekret Cloudflare Pages (§6).
3. Dodaj skrypt widgetu i div do obu formularzy — `contact.html` i
   `pl/contact.html`, wewnątrz elementu `<form>`, tuż nad przyciskiem
   wysyłania:
   ```html
   <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
   <div class="cf-turnstile" data-sitekey="YOUR_SITE_KEY_HERE"></div>
   ```
   Żadne zmiany w JavaScript nie są potrzebne — Turnstile automatycznie
   wstrzykuje token odpowiedzi do formularza, a `functions/api/contact.js`
   już go odczytuje.

---

## 17. Lista kontrolna przed uruchomieniem

- [ ] Wypchnij projekt do prywatnego repozytorium GitHub (§3)
- [ ] Utwórz projekt Cloudflare Pages i potwierdź, że podgląd `.pages.dev`
      wdraża się poprawnie bez błędów budowania (§5)
- [ ] Dodaj `RESEND_API_KEY` jako sekret Cloudflare Pages (§6, §7)
- [ ] Wyślij testowe zapytanie przez formularz na adresie `.pages.dev` i
      potwierdź, że dociera na `enquiries@cevano.co.uk` (§12)
- [ ] Przenieś DNS do Cloudflare, starannie zachowując każdy rekord
      Microsoft 365 (§9, §10)
- [ ] Podłącz zarówno `cevano.co.uk`, jak i `www.cevano.co.uk` jako domeny
      niestandardowe w projekcie Pages (§8)
- [ ] Potwierdź, że SSL jest aktywne (widoczna kłódka) na domenie
      docelowej (§11)
- [ ] Przetestuj ponownie formularz kontaktowy (oba języki) na domenie
      docelowej, nie tylko na adresie podglądowym (§12)
- [ ] Wyślij testowy e-mail na `enquiries@cevano.co.uk` z zewnętrznego
      adresu i potwierdź normalne dostarczenie przez Microsoft 365,
      niezależnie od przeniesienia DNS (§10)
- [ ] Zweryfikuj subdomenę wysyłkową w Resend i ustaw `FROM_EMAIL` dla
      produkcyjnej jakości dostarczalności, zamiast współdzielonej domeny
      testowej (§7)
- [ ] Uzupełnij pozostałe placeholdery na stronach prawnych (§15)
- [ ] Sprawdź stronę na prawdziwym telefonie: menu mobilne, przełącznik
      trybu ciemnego, przełącznik języka, formularz kontaktowy

## 18. Lista kontrolna SEO po uruchomieniu

- [ ] Zgłoś `https://www.cevano.co.uk/sitemap.xml` w Google Search Console
- [ ] Zgłoś tę samą mapę witryny w Bing Webmaster Tools
- [ ] Potwierdź, że `robots.txt` jest dostępny pod adresem
      `https://www.cevano.co.uk/robots.txt`
- [ ] Sprawdź kilka stron narzędziem Google Rich Results Test, aby
      potwierdzić, że dane strukturalne `ProfessionalService` są poprawnie
      odczytywane
- [ ] Potwierdź, że przekierowanie `www` względem domeny głównej (§8)
      działa w obie strony, zanim wyszukiwarki zaindeksują obie wersje —
      działające przekierowanie 301 od razu zapobiega problemom z
      duplikacją treści

---

## 19. Procedura wycofania zmian (rollback)

Ponieważ Cloudflare Pages zachowuje każde poprzednie wdrożenie:

1. Przejdź do **Cloudflare Pages → Twój projekt → Deployments**.
2. Znajdź na liście ostatnie znane działające wdrożenie.
3. Kliknij menu **⋯** → **Rollback to this deployment**.

To natychmiast przekierowuje środowisko produkcyjne na tę wersję — bez
potrzeby cofania w git czy nowego pusha, choć dobrą praktyką jest również
naprawienie i ponowne wypchnięcie źródła problemu w git, aby kolejne
wdrożenie go nie powtórzyło.

Alternatywnie, cofnięcie na poziomie git: `git revert <zły-commit>` i push
— to uruchamia normalne nowe wdrożenie z cofniętego stanu.

---

## 20. Rozwiązywanie problemów

**Formularz kontaktowy zwraca ogólny błąd / nic się nie dzieje:**
- Sprawdź **Cloudflare Pages → Twój projekt → Functions → Real-time Logs**
  (lub `wrangler pages deployment tail`) podczas wysyłania testowego
  zapytania — funkcja loguje dokładny błąd (np. błąd API Resend) do
  konsoli.
- Potwierdź, że `RESEND_API_KEY` jest ustawiony konkretnie dla środowiska
  **Production**, nie tylko Preview.
- Potwierdź, że wykonano ponowne wdrożenie po dodaniu/zmianie zmiennych
  środowiskowych (§6).

**E-maile w ogóle nie docierają:**
- Sprawdź zakładkę **Logs** w panelu Resend — pokazuje każdą próbę wysyłki
  i to, czy się powiodła, odbiła się, czy została odrzucona.
- Jeśli używasz zweryfikowanej subdomeny wysyłkowej, potwierdź, że jej
  rekordy DNS pokazują status "Verified" (nie "Pending") w Resend.
- Sprawdź folder spam/niechciane w skrzynce Microsoft 365 jako pierwszy
  krok.

**E-maile docierają, ale dostarczalność wydaje się słaba / trafiają do spamu:**
- Zwykle oznacza to, że nadal korzystasz ze współdzielonej domeny
  `resend.dev` — zweryfikuj własną subdomenę (§7) dla prawdziwej reputacji
  nadawcy.

**Poczta Microsoft 365 przestała działać po przeniesieniu DNS:**
- Natychmiast sprawdź DNS Cloudflare względem oryginalnej listy rekordów
  DNS Microsoft 365 (§10) — prawdopodobnie podczas importu do Cloudflare
  pominięto rekord MX, SPF lub DKIM, który trzeba dodać ręcznie z powrotem.
- Dlatego właśnie §10 istnieje jako osobna lista kontrolna — zawsze
  weryfikuj przed i po zmianie serwerów nazw, nie tylko raz.

**Strona pokazuje starą treść po pushu do GitHub:**
- Sprawdź **Cloudflare Pages → Deployments**, aby potwierdzić, że nowe
  wdrożenie faktycznie się uruchomiło i powiodło — jeśli push nie trafił do
  `main` (np. wypchnięto do innej gałęzi), żadne wdrożenie produkcyjne się
  nie odbywa.
- Odśwież stronę z wymuszeniem / wyczyść pamięć podręczną przeglądarki —
  `_headers` ustawia długi czas cache dla CSS/JS/obrazów, co świetnie
  wpływa na wydajność, ale oznacza, że przeglądarka z zapisaną starą wersją
  może wymagać wymuszonego odświeżenia.

**Strona zwraca błąd 404, mimo że nie powinna:**
- Cloudflare Pages serwuje pliki po dokładnej ścieżce — `/about.html` musi
  być zażądany dokładnie tak, jak zapisano; nie ma automatycznego
  usuwania `.html`. Potwierdź, że linki w HTML dokładnie odpowiadają
  nazwom plików (struktura linków w projekcie już to uwzględnia wszędzie).

**Widget Turnstile się nie pojawia / weryfikacja zawsze się nie udaje:**
- Potwierdź, że site key w HTML odpowiada temu widocznemu w panelu
  Cloudflare Turnstile dla dokładnie tej domeny.
- Potwierdź, że `TURNSTILE_SECRET_KEY` (klucz *sekretny*, nie site key)
  jest ustawiony jako zmienna środowiskowa Cloudflare Pages.
