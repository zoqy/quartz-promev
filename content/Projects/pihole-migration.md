---
title: Pi-hole Migration
author: Theo
created: 2026-01-10
tags: [project, networking, dns]
description: Moving DNS filtering to host networking so client stats mean something.
---

# Pi-hole Migration

**Status:** done

Under bridge networking every query arrived from the Docker gateway address, so per-client
statistics and per-client blocking were meaningless.

Host networking fixes it: the container sees real client addresses.

## Trade accepted

Host mode plus `NET_ADMIN` shortens the path from a compromised container to the host's
network stack. Accepted because the alternative doesn't work reliably over Wi-Fi.

Related: [[Topics/exposure-and-binding]] · [[Topics/docker-compose]]
