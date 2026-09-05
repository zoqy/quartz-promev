---
title: Unversioned Is Unbacked Up
author: Theo
created: 2026-01-10
tags: [note, infrastructure]
description: A file that exists on exactly one machine is not stored, it is at risk.
---

# Unversioned Is Unbacked Up

Config that lives only on the machine it configures is one disk failure from gone, and worse,
it is undocumented — nobody can read it without logging in.

The fix is boring: put it in a repo. Even a private one, even alone, even if nothing else
ever reads it.

Related: [[Projects/backup-strategy]] · [[Topics/self-hosting]]
