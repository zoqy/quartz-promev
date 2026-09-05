---
title: Homelab Networking
author: Theo
created: 2026-01-02
tags: [topic, networking, infrastructure]
description: Fixture topic note — exercises tables, code blocks, quotes and lists.
---

# Homelab Networking

Fixture content. The point of this note is the *shapes* below, not the words.

## A table wider than a phone

| Interface | Address | Role | State | Notes that run long |
|---|---|---|---|---|
| `wlp2s0` | 192.168.x.x/24 | LAN | up | The only working NIC on the machine |
| `tailscale0` | 100.x.x.x/32 | Tailnet | up | How everything is actually reached |
| `enp3s0` | — | unused | down | Failed hardware, never to be used again |
| `docker0` | 172.17.x.x/16 | bridge | down | Created by the container runtime |

## A long unbroken code line

```bash
docker run -d --name example -p 127.0.0.1:8080:8080 -v /some/very/long/path/that/keeps/going:/app/content:ro --restart unless-stopped example-image:latest
```

## Prose, links and quotes

Reaching it means `ssh somehost`, then checking [[Projects/dashboard-restyle|the project]]. A
[[People/sample-collaborator|person]] may be involved.

> A blockquote, for the styling of blockquotes. It should be distinguishable from body text
> without shouting, and it should still be readable at phone width.

1. An ordered list
2. With a second item
3. And a third that is quite a lot longer than the other two, so that it wraps onto more than one line even on a wide screen
