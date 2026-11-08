---
name: Cevano IT Solutions
description: Practical IT support, Microsoft 365 management and data analytics for small businesses.
colors:
  navy: "#001C3F"
  navy-800: "#0B2A50"
  blue: "#0072D6"
  blue-mid: "#005EBB"
  blue-light: "#0092E6"
  bg: "#F5F8FC"
  bg-alt: "#EBF1F8"
  deep: "#0F172A"
  deep-2: "#172D4A"
  on-deep: "#E8EEF8"
  on-deep-2: "#AFC0DA"
  hero-accent: "#7CC0FF"
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
    fontFamily: "Sora, Segoe UI, sans-serif"
    fontSize: "clamp(2.1rem, 4vw, 3.2rem)"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Sora, Segoe UI, sans-serif"
    fontSize: "clamp(1.65rem, 3vw, 2.2rem)"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Sora, Segoe UI, sans-serif"
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
  s: "8px"
  m: "14px"
  l: "20px"
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

**Creative North Star: "The Glass Office"**

Cevano opens on a dark, glassy first screen and then settles into a calm, light office. The hero is deep navy over a darkened photograph of a real open-plan office, with a soft blue light from the top right. On it sit four frosted glass cards that show the four services as small, honest interface sketches: a Microsoft 365 user list, an IT support queue, a website in a browser and a phone, a Power BI style dashboard. Below the hero the page turns light: white cards with hairline borders and soft shadows on a pale blue-grey ground, one layout per section, never a second bento.

The look is premium through restraint. Glass appears only in the hero. Gradients are only the hero wash, the CTA banner and faint blue tints behind icons. Motion is a 3px lift on linked cards and a short rise as blocks below the fold arrive; nothing is ever hidden at rest.

Both themes are first-class. The hero and the closing banner are dark in both; the light sections swap to night-navy surfaces in dark mode with the same structure.

**Key Characteristics:**
- Dark glass hero on a navy-washed office photograph, light content sections below.
- A bento of four service mock-ups drawn in HTML/SVG, no product logos, no figures.
- White cards (14px corners) with a hairline border and a soft two-layer shadow.
- Sora headings over Public Sans body; one h2 size, one h3 size.
- Calm motion: 3px lift on linked cards, a short rise on entry, reduced-motion respected.

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

**The Dark Bookends Rule.** Deep navy (`deep`) fills exactly two places on the home page: the hero at the top and the CTA banner before the footer. Every section between them is light. Text on deep navy uses `on-deep` (headings, body) and `on-deep-2` (secondary), and the hero accent `hero-accent` for the h1 tail and icons.

## Typography

**Display Font:** Sora (with Segoe UI, sans-serif)
**Body Font:** Public Sans (with Segoe UI, sans-serif)

**Character:** Sora gives headings a wide, geometric shape that echoes the extended CEVANO wordmark: modern and technical without the quirks of a display face. Public Sans keeps reading plain, neutral and easy. On the home hero the Polish H1 is set smaller than the English one on wide screens so both read as three parts.

### Hierarchy
- **Display** (600, clamp(2.1rem, 4vw, 3.2rem), 1.15): home hero h1 only, capped at 14ch so it breaks into short lines. Inner page h1 uses clamp(1.9rem, 3.4vw, 2.6rem), capped at 20ch.
- **Headline** (600, clamp(1.65rem, 3vw, 2.2rem), 1.15): every content h2, one size (section heads, service detail sections, the closing banner).
- **Title** (600, 1.25rem, 1.15): every card, step and problem h3, one size, always at least 1.3× below h2. Label-style headings (panel titles, contact-page block titles) are the only exception and are set like Labels.
- **Body** (400, 17px, 1.6): paragraphs in Slate, max 62ch. Card and list text is 16px, never smaller for running text. Lede is 1.15rem, max 46ch.
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
**The Two Depths Rule.** Light-section cards sit on `--shadow-card` (a 1px contact shadow plus a soft 24px blur) and rise to `--shadow-lift` on hover. Hero cards are glass: a translucent white gradient, a 14% white border, a 14px backdrop blur and a deep shadow. Glass is never used outside the hero; under `prefers-reduced-transparency` the blur is replaced by an opaque navy fill.

## Shapes

Softly rounded, never pill-shaped except small status pills. Controls (buttons, inputs) use 8px (`rounded.s`). Cards and panels use 14px (`rounded.m`). Hero glass cards, the problem panel and the CTA banner use 20px (`rounded.l`). Icon tiles are 12px squares. Borders stay 1px hairlines.

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
- **Service grid (signature):** no card boxes. Cells divided by hairlines, in service-priority order. Microsoft 365 is a full-width lead cell: copy on the left, its four concrete outcomes as a check list on the right (Ink text). Below it, three equal cells: Websites & Landing Pages, IT Support, Data Analytics & Power BI. Ghost links name their target ("Microsoft 365 in detail →"), never a bare "Learn more". The ghost link is stretched over its cell, so the whole cell is the click target and the hover lift is honest. On hover a cell gains white surface, a 3px inset Working Blue top bar and a 2px lift. Each cell has a small line icon, Title, Slate copy and a ghost "Learn more →".
- **Secondary cards:** white surface, hairline border, 8px corners, 26px 24px padding. Static: no hover effect, because they are not links. Lists use small Signal Blue square bullets.
- **Problem grid (home):** ruled 2×2 grid in the service-grid hairline language, one column at ≤760px. Each cell is a real Microsoft 365 problem as an h3 ("An important email never arrived") and what we do about it in one or two sentences. Only problems from PRODUCT.md's confirmed task list.
- **Review offer:** Filing Grey-Blue band with hairline border and 8px corners under the problem grid: a question, one line offering the free Microsoft 365 review, and an outline button. Never describe the review's scope beyond "review your setup and say what to fix first".
- **Panel:** Filing Grey-Blue fill, hairline border, 8px, 28px padding, dashed dividers between items.
- **CTA banner:** solid Office Navy, 8px, 48px 44px, white headline, a faint (6% white) bar-chart motif bottom right.

### Inputs / Fields
- **Style:** Morning Paper fill, hairline border, 4px corners, 12px 14px, 16px text (never smaller: iOS zooms below 16px). Labels 14px 700 Ink above the field; required asterisk in Deep Working Blue.
- **Focus:** border goes transparent, 2px Signal Blue outline at 1px offset.
- **Hint:** 14px Slate line between label and field, linked with `aria-describedby`. Guidance lives next to the field it is about.
- **Checkbox:** 20px, `accent-color` Working Blue.
- **Confirmation panel:** on success the form is replaced (not cleared under a status box) by a panel: an "Enquiry sent" h2 that takes focus, the visitor's email, a copy of their message in a Morning Paper box (text only, never HTML), and two actions: an outline "Send another enquiry" button and a ghost link back to services. Also used for the no-JS `?sent=1` return.
- **Service preselect:** links to `contact.html?service=m365|website|it-support|data` pre-select the matching option; unknown values are ignored. Each core service section on services.html ends with an outline "Ask about …" button using this.
- **Status:** full-width message block directly under the submit button, 4px corners, tinted green or red with matching border. Success uses `role=status`; error uses `role=alert` and ends with a real mailto link.

### Navigation
- **Header:** sticky white bar with a hairline bottom border, 60px logo (light/dark variants). Links 15px 600 Slate. Hover and current page turn Ink with a 2px Working Blue underline.
- **Language switch:** "EN | PL" in 14px 700; active language in Working Blue.
- **Theme toggle:** 38px hairline circle with moon/sun icon.
- **Mobile (≤900px):** logo drops to 48px; a small primary "Get in touch" stays in the header next to a 44px menu button. The menu button swaps to a close icon when open; Esc closes the menu and returns focus. The panel fades and slides in 8px; links become full-width rows with hairline dividers.

### Process Steps
Three columns, each with a 40px navy disc (dark: `dark-blue`) holding a Sora number, joined by hairline connectors on desktop.

### Hero Bento (signature)
Four linked glass cards on the dark hero, four shapes: Microsoft 365 & Security tall on the left, IT Support and Web Design stacked on the right, Data Analytics & Power BI across the bottom. Each card has a 20px icon in `hero-accent`, a Sora 15px title, an arrow that slides 3px on hover, and a small mock-up built from HTML/SVG: user rows with "MFA on / Licensed / Offboarded" pills; a support list with status dots; a browser window with a phone over its corner; KPI tiles with a bar chart and trend line. Mock-ups use placeholder bars, never names, numbers or third-party logos, and are `aria-hidden`. Each card links to its section on services.html. At 600px and below the grid becomes M365 full width, IT and web side by side, data full width, and each mock-up drops its least important row.

### Hero Photograph
Pexels photo 6794970, "Open space office with tables" by Max Vakhtbovych (Pexels licence, free for commercial use). Stored as `assets/img/hero/office-{768,1280,1920}.webp` with a 1280px JPG fallback, `fetchpriority="high"`, covered by a navy wash so all hero text reads at 7:1 or better.

### Next Steps
Small numbered list on the contact page: 20px hairline circles with Deep Working Blue Sora numerals, 15px Slate text.

### Credential Badge
Inline 13.5px 600 Slate line with a 16px Deep Working Blue rosette icon. Used once, for "Microsoft Certified: Power BI Data Analyst Associate (PL-300)" in the Data Analytics section. Name of the credential only: no link, no holder name.

### Footer
Office Navy (dark: `footer-dark`) with four columns: brand blurb plus company number and address, then Company, Services and Legal link lists. Muted blue-grey text, white on hover; hairline-ringed circular social icons.

## Do's and Don'ts

### Do:
- **Do** use the shared light card (white surface, hairline border, `--shadow-card`, 14px corners) for cards in light sections, and give each section its own layout.
- **Do** reserve Working Blue (`#0072D6`) for things a visitor can click.
- **Do** keep corners at 8px for controls, 14px for cards and 20px for large panels and hero cards.
- **Do** keep motion to a 3px lift on linked cards (0.2s), a short rise (0.6s) for blocks entering below the fold, and nothing under `prefers-reduced-motion`.
- **Do** let the home hero fill the first screen under the header (capped at 900px), so the next section's heading is never cut by the fold.
- **Do** design every new element for both light and dark themes using the existing CSS variables.
- **Do** keep text in sentence case, with headings capped in `ch` and paragraphs at 62ch.
- **Do** give every control at least a 44px touch target at ≤900px, even when the visible mark is smaller.
- **Do** list the four services as Microsoft 365, IT Support, Web Design, Data Analytics & Power BI on the home page (hero bento and services section).

### Don't:
- **Don't** use glass, blur or glow outside the hero.
- **Don't** use pure black text or pure grey neutrals; neutrals stay cool blue-grey.
- **Don't** add dark bands between the hero and the closing banner; middle sections stay light.
- **Don't** add uppercase tracked micro-labels, real product logos in the mock-ups, or figures that look like customer data.
- **Don't** round anything beyond 20px, and never make buttons pill-shaped.
- **Don't** show team or office-staff imagery, or any personal name or photo; the business is one person and the site stays impersonal (see PRODUCT.md).
- **Don't** put white text on `dark-blue-mid`; it fails contrast.
- **Don't** give hover lift, fill or border changes to anything that is not a link or button.
- **Don't** hide content in CSS while waiting for a script; the entrance animation only plays on blocks a script has marked, so content is visible if the script never runs.
