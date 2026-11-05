---
name: Cevano IT Solutions
description: Practical IT support, Microsoft 365 management and data analytics for small businesses.
colors:
  navy: "#001C3F"
  navy-800: "#0B2A50"
  blue: "#0072D6"
  blue-mid: "#005EBB"
  blue-light: "#0092E6"
  bg: "#F6F8FB"
  bg-alt: "#EDF1F7"
  surface: "#FFFFFF"
  ink: "#0B1B33"
  slate: "#4A5A75"
  line: "#DCE3EE"
  focus-ring: "#0092E6"
  dark-bg: "#071120"
  dark-bg-alt: "#0B1830"
  dark-surface: "#0D1B30"
  dark-ink: "#E7ECF6"
  dark-slate: "#93A3C0"
  dark-line: "#1E2D46"
  dark-blue: "#1A66B3"
  dark-blue-mid: "#3D97F2"
  footer-dark: "#050C18"
  btn-hover: "#005EBB"
  dark-btn-hover: "#1F74C9"
  on-navy: "#C9D4E8"
  on-navy-soft: "#B9C6DE"
  on-navy-muted: "#93A3C0"
  on-navy-faint: "#8092AF"
  success-bg: "#E7F5EC"
  success-ink: "#1B6E3C"
  error-bg: "#FBEAEA"
  error-ink: "#B23A3A"
typography:
  display:
    fontFamily: "Space Grotesk, Segoe UI, sans-serif"
    fontSize: "clamp(2.1rem, 4vw, 3.2rem)"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Space Grotesk, Segoe UI, sans-serif"
    fontSize: "clamp(1.6rem, 3vw, 2.2rem)"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Space Grotesk, Segoe UI, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Public Sans, Segoe UI, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Public Sans, Segoe UI, sans-serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1.4
rounded:
  s: "4px"
  m: "8px"
  pill: "20px"
  full: "50%"
spacing:
  gutter: "24px"
  card: "28px"
  block: "48px"
  layout-gap: "56px"
  section: "84px"
  maxw: "1180px"
  header-h: "89px"
  header-h-mobile: "77px"
  touch-target: "44px"
components:
  button-primary:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.surface}"
    rounded: "{rounded.s}"
    padding: "12px 22px"
    typography: "{typography.label}"
  button-primary-hover:
    backgroundColor: "{colors.btn-hover}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.s}"
    padding: "12px 22px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.blue-mid}"
    padding: "12px 4px"
  button-sm:
    padding: "9px 16px"
  input:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.ink}"
    rounded: "{rounded.s}"
    padding: "12px 14px"
  card-subservice:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.m}"
    padding: "26px 24px"
  form-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.m}"
    padding: "32px"
  panel:
    backgroundColor: "{colors.bg-alt}"
    rounded: "{rounded.m}"
    padding: "28px"
  cta-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.surface}"
    rounded: "{rounded.m}"
    padding: "48px 44px"
  chip-area:
    textColor: "{colors.slate}"
    rounded: "{rounded.pill}"
    padding: "5px 12px"
  service-lead:
    padding: "44px 30px"
  next-steps-marker:
    textColor: "{colors.blue-mid}"
    rounded: "{rounded.full}"
    size: "20px"
  step-number:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.surface}"
    rounded: "{rounded.full}"
    size: "40px"
---

# Design System: Cevano IT Solutions

## Overview

**Creative North Star: "The Tidy Office"**

Cevano looks the way a well-run small office feels after a good IT provider has been through it: ordered, labelled, calm, nothing left lying around. The system promises "properly managed" before a word is read. Pale blue-grey ground, white surfaces, hairline rules and a deep navy anchor do the organising. One bright working blue marks the things you can act on.

Density is moderate and generous with air. Sections breathe at 84px, content sits in a 1180px container, and paragraphs stop at 62ch. Structure is drawn with lines rather than boxes wherever possible: the core services sit in a ruled grid, not floating cards. Decoration is limited to small, quiet line icons and an abstract chart motif that hints at the data work without becoming illustration.

Light and dark themes are both first-class. Dark mode is a deep night-navy, not grey, and keeps the same ruled structure.

**Key Characteristics:**
- Navy anchor, single working blue for action, cool blue-grey neutrals.
- Space Grotesk headings over Public Sans body.
- Hairline 1px rules carry structure; shadows are almost absent.
- Small, crisp corners (4px controls, 8px containers).
- Calm motion: short colour fades and a 2px lift on hover only.

## Colors

A cool, low-chroma navy-and-blue palette where blue appears only where something can be done.

### Primary
- **Working Blue** (`blue`): primary buttons, active nav underline, the inset top bar on hovered service cards. The one colour that means "act here".
- **Deep Working Blue** (`blue-mid`): primary button hover in light theme (via `btn-hover`), active language, text links, eyebrows and kickers, check-list icons, required-field asterisks. Carries blue at text size with enough contrast.
- **Signal Blue** (`blue-light`): small accents only: bullet squares, flow-row dots, service step numbers, hover border on secondary cards, focus ring.

### Secondary
- **Office Navy** (`navy`): the anchor. Footer, CTA banner, process step discs, skip link. Large calm fields of navy close the page.
- **Navy 800** (`navy-800`): reserved deeper brand tone.

### Neutral
- **Morning Paper** (`bg`): page background, a faintly blue off-white. Also input fill.
- **Filing Grey-Blue** (`bg-alt`): alternate section bands, panels, hover fill on why-cards, active mini-nav pill.
- **Clean Surface** (`surface`): header, cards, form card, cookie banner.
- **Ink** (`ink`): headings and strong text. A navy-black, never pure black.
- **Slate** (`slate`): body copy, nav links at rest, secondary text.
- **Hairline** (`line`): every border and rule. The main structural tool.

### Dark theme
Swaps neutrals for night-navy (`dark-bg`, `dark-bg-alt`, `dark-surface`), light ink (`dark-ink`, `dark-slate`) and `dark-line`. Blue shifts to `dark-blue` and `dark-blue-mid` for contrast. Footer goes to `footer-dark`. The CTA banner becomes a bordered surface instead of solid navy.

White text only ever sits on `dark-blue` (5.8:1) or `dark-btn-hover` (4.8:1) in dark mode, never on `dark-blue-mid` (3.0:1). `dark-blue-mid` is for blue text and icons on dark surfaces.

### On navy
Footer and CTA-banner text use the `on-navy` family (`on-navy`, `on-navy-soft`, `on-navy-muted`, `on-navy-faint`). These stay the same in both themes. Never hard-code another grey on navy; `on-navy-faint` (5:1) is the floor.

### Status
Form feedback only: `success-bg`/`success-ink` and `error-bg`/`error-ink`, each with a matching tinted border and dark-theme equivalents in CSS.

### Named Rules
**The Blue Means Act Rule.** Working Blue fills only interactive elements. Decorative blue stays at Signal Blue and small sizes (dots, bullets, icons).

**The Navy Bookend Rule.** Navy appears as large fields only at the end of a page (CTA banner, footer) and in small solid marks (step discs). It never fills a hero or mid-page band.

## Typography

**Display Font:** Space Grotesk (with Segoe UI, sans-serif)
**Body Font:** Public Sans (with Segoe UI, sans-serif)

**Character:** Space Grotesk gives headings a technical, slightly engineered edge. Public Sans keeps reading plain, neutral and government-form clear. Together: competent but not cold.

### Hierarchy
- **Display** (600, clamp(2.1rem, 4vw, 3.2rem), 1.15): home hero h1 only, capped at 14ch so it breaks into short lines. Inner page h1 uses clamp(1.9rem, 3.4vw, 2.6rem), capped at 20ch.
- **Headline** (600, clamp(1.6rem, 3vw, 2.2rem), 1.15): section h2. Detail sections use 1.7rem.
- **Title** (600, 1.05–1.25rem, 1.15): card and step h3.
- **Body** (400, 17px, 1.6): paragraphs in Slate, max 62ch. Card text steps down to 14.5–15px. Lede is 1.15rem, max 46ch.
- **Label** (700, 13–15px): eyebrows and kickers in Deep Working Blue, form labels in Ink, buttons, nav (600, 15px). Sentence case; no uppercase tracking.

### Named Rules
**The Sentence Case Rule.** Labels, eyebrows and buttons stay in sentence case at weight 700. Small uppercase tracked labels are not part of this system.

**The Short Line Rule.** Headlines carry a `ch` cap (14–20ch) and paragraphs stop at 62ch. Headings use `text-wrap: balance` and paragraphs `text-wrap: pretty`, so no word is left alone on a last line.

## Layout

Single 1180px container with 24px gutters. Sections use 84px vertical padding; inner page heroes 56–60px; detail service blocks 64px. Section heads are capped at 640px with 48px below.

Grids are simple: three columns for services, secondary services and process steps; asymmetric two-column splits (about 1.05fr/0.85fr hero, 1.1fr/0.9fr contact, 0.9fr/1.1fr detail) with 48–56px gaps. Why-cards use `auto-fit, minmax(220px, 1fr)`.

The sticky header height is a token (`--header-h`: 89px, 77px at ≤900px). The mobile menu panel and the services sub-nav sit exactly at that offset.

Responsive: main nav collapses into a full-screen panel at 900px. The hero visual moves below the copy at ≤900px and is hidden at ≤600px, so the headline and both actions fit the first phone screen. On the contact page the form comes first at ≤900px. Grids drop to one column at 860px. Footer goes from four columns to two at 860px and one at 540px. Two-field form rows stack at 600px. The services page has a sticky pill mini-nav under the header.

## Elevation & Depth

Flat by default. Depth comes from tonal layering (Morning Paper ground, white surface, Filing Grey-Blue bands) and hairline borders, not shadows. The base shadow token is nearly invisible.

### Shadow Vocabulary
- **Resting** (`box-shadow: 0 1px 2px rgba(11,27,51,0.04)`): token default; barely there.
- **Hover lift** (`box-shadow: 0 8px 20px rgba(11,27,51,0.06)`, dark: `rgba(0,0,0,0.25)`): secondary cards on hover, paired with `translateY(-2px)`.
- **Inset bar** (`box-shadow: inset 0 3px 0 var(--blue)`): service card hover; reads as a tab marker, not depth.
- **Floating** (`box-shadow: 0 8px 30px rgba(0,10,30,0.18)`): cookie banner only, the one element that floats over content.

### Named Rules
**The Flat-At-Rest Rule.** Nothing casts a visible shadow at rest except the cookie banner. Shadows appear only as a hover response.

## Shapes

Crisp, small corners. Controls (buttons, inputs, status messages) use 4px. Containers (cards, form card, panels, CTA banner, cookie banner) use 8px. Pills (20px) are used only for area tags and the services mini-nav. Circles are used for the theme toggle, social icons and process step discs. Bullets are tiny 6px squares with 1px corners. Borders are always 1px hairlines; panels use a dashed hairline between list items.

## Components

### Buttons
Crisp and restrained.
- **Shape:** gently squared (4px).
- **Primary:** Working Blue fill, white 700 text at 15px, 12px 22px padding. Hover moves to `btn-hover` (Deep Working Blue in light, `dark-btn-hover` in dark). Press nudges down 1px.
- **Outline:** transparent with a hairline border and Ink text. Hover turns border and text Working Blue.
- **Ghost:** Deep Working Blue text link-button with an arrow ("Learn more →"), horizontal padding 4px.
- **Small:** 9px 16px, 14px text (header "Get in touch").
- **On navy:** inside the CTA banner the primary flips to a white fill with navy text.
- **Focus:** 2px Signal Blue outline, 2px offset, site-wide.

### Chips
- **Area tags:** 13px 600 Slate text, hairline border, pill shape, 5px 12px. Static labels, not filters.
- **Mini-nav pills:** transparent at rest; active pill gets Filing Grey-Blue fill, hairline border and Deep Working Blue text.

### Cards / Containers
- **Service grid (signature):** no card boxes. Cells divided by hairlines, in service-priority order. Microsoft 365 is a full-width lead cell: copy on the left, its four concrete outcomes as a check list on the right (Ink text). Below it, three equal cells: Websites & Landing Pages, IT Support, Data Analytics & Power BI. Ghost links name their target ("Microsoft 365 in detail →"), never a bare "Learn more". On hover a cell gains white surface, a 3px inset Working Blue top bar and a 2px lift. Each cell has a small line icon, Title, Slate copy and a ghost "Learn more →".
- **Secondary cards:** white surface, hairline border, 8px corners, 26px 24px padding. Hover: Signal Blue border, 2px lift, soft shadow. Lists use small Signal Blue square bullets.
- **Why grid:** tiles separated by 1px gaps over a Hairline background inside one 8px rounded frame. Hover fills tile with Filing Grey-Blue.
- **Panel:** Filing Grey-Blue fill, hairline border, 8px, 28px padding, dashed dividers between items.
- **CTA banner:** solid Office Navy, 8px, 48px 44px, white headline, a faint (6% white) bar-chart motif bottom right.

### Inputs / Fields
- **Style:** Morning Paper fill, hairline border, 4px corners, 12px 14px, 16px text (never smaller: iOS zooms below 16px). Labels 14px 700 Ink above the field; required asterisk in Deep Working Blue.
- **Focus:** border goes transparent, 2px Signal Blue outline at 1px offset.
- **Hint:** 14px Slate line between label and field, linked with `aria-describedby`. Guidance lives next to the field it is about.
- **Checkbox:** 20px, `accent-color` Working Blue.
- **Status:** full-width message block directly under the submit button, 4px corners, tinted green or red with matching border. Success uses `role=status`; error uses `role=alert` and ends with a real mailto link.

### Navigation
- **Header:** sticky white bar with a hairline bottom border, 60px logo (light/dark variants). Links 15px 600 Slate. Hover and current page turn Ink with a 2px Working Blue underline.
- **Language switch:** "EN | PL" in 14px 700; active language in Working Blue.
- **Theme toggle:** 38px hairline circle with moon/sun icon.
- **Mobile (≤900px):** logo drops to 48px; a small primary "Get in touch" stays in the header next to a 44px menu button. The menu button swaps to a close icon when open; Esc closes the menu and returns focus. The panel fades and slides in 8px; links become full-width rows with hairline dividers.

### Process Steps
Three columns, each with a 40px navy disc (dark: `dark-blue`) holding a Space Grotesk number, joined by hairline connectors on desktop.

### Hero User-List Panel (signature)
The home hero shows a simplified Microsoft 365 user list instead of illustration: an 8px hairline frame on Clean Surface, a header with the four-square M365 mark, four rows of placeholder bars (never invented names) and status pills ("Licensed", "MFA on", and one dimmed, dashed "Offboarded" row with a lock). Pills are 24px tall, fully rounded, Filing Grey-Blue with a Deep Working Blue check. Labels are translated per language. Decorative: `aria-hidden`.

### Next Steps
Small numbered list on the contact page: 20px hairline circles with Deep Working Blue Space Grotesk numerals, 15px Slate text.

### Credential Badge
Inline 13.5px 600 Slate line with a 16px Deep Working Blue rosette icon. Used once, for "Microsoft Certified: Power BI Data Analyst Associate (PL-300)" in the Data Analytics section. Name of the credential only: no link, no holder name.

### Footer
Office Navy (dark: `footer-dark`) with four columns: brand blurb plus company number and address, then Company, Services and Legal link lists. Muted blue-grey text, white on hover; hairline-ringed circular social icons.

## Do's and Don'ts

### Do:
- **Do** draw structure with 1px Hairline rules and tonal bands before reaching for boxes or shadows.
- **Do** reserve Working Blue (`#0072D6`) for things a visitor can click.
- **Do** keep corners at 4px for controls and 8px for containers.
- **Do** keep hover motion to colour fades (0.15–0.18s) and a 2px lift; honour `prefers-reduced-motion`.
- **Do** design every new element for both light and dark themes using the existing CSS variables.
- **Do** keep text in sentence case, with headings capped in `ch` and paragraphs at 62ch.
- **Do** give every control at least a 44px touch target at ≤900px, even when the visible mark is smaller.
- **Do** list services in priority order everywhere: Microsoft 365, Websites & Landing Pages, IT Support, Data Analytics & Power BI.

### Don't:
- **Don't** add shadows at rest; only the cookie banner floats.
- **Don't** use pure black text or pure grey neutrals; neutrals stay cool blue-grey.
- **Don't** fill heroes or mid-page bands with navy; navy closes the page.
- **Don't** add uppercase tracked micro-labels.
- **Don't** use large corner radii (above 8px) on cards or buttons.
- **Don't** show team or office-staff imagery, or any personal name or photo; the business is one person and the site stays impersonal (see PRODUCT.md).
- **Don't** put white text on `dark-blue-mid`; it fails contrast.
