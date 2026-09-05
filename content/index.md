---
title: Welcome to the Vault
author: Theo
created: 2026-01-01
tags: [meta, index]
description: Local fixture content — invented notes used for styling work.
---

# Prometheus Vault

**This is fixture content, not the real vault.** Every note in `content/` here is invented. The
real vault lives on the homelab and is bind-mounted over this directory at run time, so nothing
here ever reaches a deployed instance — `.dockerignore` also keeps it out of the image.

Fixtures rather than real notes, for two reasons. Personal notes shouldn't be in a public repo.
And invented ones are *better* for styling: they're stable, they're committed so a layout
regression is reproducible, and they can deliberately contain the awkward cases real notes only
produce by accident.

## Sections

- [[Topics/homelab-networking|Topics]] — concepts and how things work
- [[People/sample-collaborator|People]] — who is involved in what
- [[Projects/dashboard-restyle|Projects]] — things being built
- [[Notes/a-note-with-a-deliberately-long-title-that-should-wrap-awkwardly|Notes]] — loose thoughts
- [[Consumed Media/sample-article|Consumed Media]] — things read or watched

## The deliberately awkward ones

A few fixtures exist purely to break layouts: an over-long title, a table wider than a phone, an
unbreakable string, a four-deep list. If the design survives those, it survives real notes.
