---
title: Exit Codes Are Not All Failures
author: Theo
created: 2026-01-10
tags: [note, linux, debugging]
description: A non-zero exit can be a deliberate signal, and alerting on all of them cries wolf.
---

# Exit Codes Are Not All Failures

A supervisor that alerts on every non-zero exit will eventually alert on something the
program meant.

`75` is `EX_TEMPFAIL` from `sysexits.h`. Plenty of software uses it to mean *restart me* — a
request, not a crash. If the alerting path doesn't check the code, every intentional restart
becomes an incident, and incidents nobody believes are worse than no incidents.

> The value of an alert is inversely proportional to how often it is wrong.

Related: [[Topics/systemd-timers]] · [[Notes/on-writing-for-your-future-self]]
