---
title: Docker Compose
author: Theo
created: 2026-01-10
tags: [topic, docker, infrastructure]
description: Declaring a service so it can be rebuilt from nothing.
---

# Docker Compose

One file describing what runs, what it mounts, and what it publishes.

```yaml
services:
  example:
    build: .
    restart: unless-stopped
    ports:
      - "100.x.x.x:8080:8080"
    volumes:
      - /home/user/data:/app/content:ro
```

## Habits worth keeping

- `restart: unless-stopped` so a reboot doesn't lose the service
- read-only mounts wherever the container has no business writing
- the bind address written out in full — see [[Topics/exposure-and-binding]]

Related: [[Topics/systemd-timers]] · [[Topics/self-hosting]]
