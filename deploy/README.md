# deploy/

Everything needed to turn this fork into a running container. Kept in its own directory so
`git merge upstream/v5` never conflicts with upstream's own `Dockerfile`.

| File | What it is |
|---|---|
| `Dockerfile` | Builds the image from this repo. Two-stage, mirroring upstream's layer caching. |
| `entrypoint.sh` | Rewrites `baseUrl` from the environment, then starts Quartz. |

## What is *not* here

`docker-compose.yml`. This repo is **public**; the compose file carries the tailnet bind
address and the vault's path on the host. It lives with the private deployment config
instead. Keep it that way — see below.

## The `baseUrl` split

`baseUrl` must be in `quartz.config.yaml` at build time: Quartz v5 has no `--baseUrl` flag on
`build` (only on `create`), and does no environment substitution when loading config.

So the committed value is the **local-dev** one, `localhost:8080`, and `entrypoint.sh`
overwrites it at container start from `QUARTZ_BASE_URL`.

This is not only a privacy workaround — `baseUrl` genuinely differs between local development
and any deployment, so it belongs to deployment either way.

If a mistake slips through, the blast radius is small: `baseUrl` only affects **absolute**
URLs (Open Graph tags, RSS, sitemap). Internal links are relative, so a wrong value produces
bad social previews, not a broken site.

## Building

```bash
docker build -f deploy/Dockerfile -t promev-quartz .
```

Run it with the vault mounted read-only and `QUARTZ_BASE_URL` set — from the private compose
file, not from here.

## Things that would leak if enabled

Two config fields are currently harmless but would gain host or account identifiers if turned
on, at which point they need the same treatment as `baseUrl`:

- `analytics:` — no domain or key set today; a self-hosted Plausible instance would add one.
- `giscus` comments — disabled today; enabling it embeds repository and category IDs.
