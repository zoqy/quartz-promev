---
title: Backup Strategy
author: Theo
created: 2026-01-10
tags: [project, infrastructure]
description: What would actually survive the disk dying tonight.
---

# Backup Strategy

**Status:** partial

The honest question is not "is there a backup" but "what would survive right now".

| Thing | Off-box copy? |
|---|---|
| Vault notes | git, pushed |
| Service source | git, pushed |
| Deployment config | on the box only — the gap |
| Container images | rebuildable from source |

Anything reachable only by SSH is not backed up; it is merely somewhere else for now.

Related: [[Topics/self-hosting]] · [[Notes/unversioned-is-unbacked-up]]
