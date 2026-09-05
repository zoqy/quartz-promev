---
title: systemd Timers
author: Theo
created: 2026-01-10
tags: [topic, linux, infrastructure]
description: Scheduled work on Linux, and the ways it surprises you.
---

# systemd Timers

Cron's replacement: a `.timer` unit triggering a `.service` unit.

## Traps

- **`disable` does not stop a running unit.** It removes the boot symlink. A unit with
  `Restart=on-failure` will keep relaunching regardless.
- **`mask` fails** while a real unit file sits at that path — it wants to symlink the path to
  `/dev/null`. Move the file instead.
- `OnFailure=` fires on *any* non-zero exit, including exit codes a program uses to mean
  something deliberate.

Related: [[Topics/docker-compose]] · [[Notes/exit-codes-are-not-all-failures]]
