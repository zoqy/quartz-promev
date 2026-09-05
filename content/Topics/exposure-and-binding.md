---
title: Exposure and Binding
author: Theo
created: 2026-01-10
tags: [topic, security, networking]
description: The difference between what a service intends and what it actually listens on.
---

# Exposure and Binding

A service's *access path* and its *listener* are different things, and confusing them is how
things end up unintentionally public.

## The lesson

Binding to `0.0.0.0` means every interface — LAN, VPN, and any globally routable address the
machine happens to have. Intending to use something over a VPN does not restrict it to one.

| Published as | Reachable from |
|---|---|
| `8080:8080` | every interface, including public IPv6 |
| `100.x.x.x:8080:8080` | the tailnet only |
| `127.0.0.1:8080:8080` | the host only |

Check with `ss -tulnp`, not with intent.

Related: [[Topics/tailscale]] · [[Topics/docker-compose]] · [[Projects/vault-dashboard]]
