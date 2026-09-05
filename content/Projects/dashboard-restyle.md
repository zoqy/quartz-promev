---
title: Dashboard Restyle
author: Theo
created: 2026-01-04
tags: [project, design, frontend]
description: Fixture project note — the work this fixture set exists to support.
---

# Dashboard Restyle

## Known defects, measured

Measured in a browser at a 327px viewport on the pre-fork deployment, before any styling work:

- **31px horizontal overflow.** `.left.sidebar`, `.center` and `article` all computed to
  `342.222px` starting at `left: 16`, ending at 358 against a `clientWidth` of 327. `body` had
  `overflow-x: visible`, so the page scrolled sideways rather than clipping.
- **Header collision.** `.page-title` got 155px starting at x=50; `.search` started at x=205,
  directly adjacent. The title wrapped to three lines and pushed into the search box.

## Checklist

- [ ] No horizontal scroll at 320px
- [ ] Header readable at 320px
- [ ] Tables scroll inside their own container, not the page
- [ ] Long code lines don't widen the page
- [ ] Unbreakable strings don't widen the page
- [ ] Still correct at laptop width
