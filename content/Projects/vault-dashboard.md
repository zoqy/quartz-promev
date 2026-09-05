---
title: Vault Dashboard
author: Theo
created: 2026-01-10
tags: [project, infrastructure, web]
description: Serving the vault as a browsable site on the tailnet.
---

# Vault Dashboard

**Status:** running

Quartz renders this vault and serves it to any device on the tailnet.

## Shape

- Source lives in a forked repo; the image is built from it
- The vault is bind-mounted **read-only** — the renderer never writes to notes
- Ports publish on the tailnet address only ([[Topics/exposure-and-binding]])

## Open

- [ ] Styling pass for phone width — [[Projects/dashboard-restyle]]
- [ ] Decide whether the build moves to a registry

Related: [[Topics/obsidian-and-quartz]] · [[Topics/docker-compose]]
