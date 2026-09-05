---
title: Tailscale
author: Theo
created: 2026-01-10
tags: [topic, networking]
description: Mesh VPN — how every machine here actually reaches every other one.
---

# Tailscale

A WireGuard mesh. Every device gets a stable address on a private tailnet, reachable from
anywhere without opening a single port to the internet.

## Why it matters here

Nothing in this homelab is exposed publicly. Services bind to the tailnet address and stay
invisible to the LAN and the outside world — see [[Topics/exposure-and-binding]].

- MagicDNS gives machines names instead of addresses
- ACLs scope who can reach what
- Subnet routers can bridge a whole LAN, though that's rarely wanted

Related: [[Topics/self-hosting]] · [[Projects/vault-dashboard]]
