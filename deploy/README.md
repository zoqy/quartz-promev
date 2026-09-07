# deploy/

Everything needed to turn this fork into a running container. Kept in its own directory so
`git merge upstream/v5` never conflicts with upstream's own `Dockerfile`.

| File | What it is |
|---|---|
| `Dockerfile` | Builds the image from this repo. Two-stage, mirroring upstream's layer caching. |
| `entrypoint.sh` | Rewrites `baseUrl` from the environment, then starts Quartz. |
| `compose.example.yml` | Template to copy. Every value is a placeholder. |
| `lightserve.py` | Local dev only. Serves an already-built `public/` in a few MB. |

`lightserve.py` exists because `npx quartz build --serve --watch` runs esbuild plus a file
watcher and sits around 250–500 MB; on a machine under memory pressure it gets OOM-killed
mid-session. It serves the finished directory instead, with no watcher and no rebuild:

```bash
npx quartz build --output public      # rebuild after any change
python deploy/lightserve.py 8080 public
```

It is not used in the container — the deployed site needs the watcher, because the vault is a
bind mount that changes underneath it.

## Install anywhere

```bash
git clone https://github.com/zoqy/quartz-promev.git && cd quartz-promev
docker build -f deploy/Dockerfile -t promev-quartz .

cp deploy/compose.example.yml /somewhere/private/compose.yml
# fill in <VPN_IP>, <PATH_TO_VAULT> and <HOSTNAME_OR_IP>, then
docker compose -f /somewhere/private/compose.yml up -d
```

Nothing else is needed. The image carries no notes — `deploy/Dockerfile` deletes `content/`
during the build, so a missing vault mount fails visibly instead of quietly serving whatever
fixture content happened to be in the checkout.

## What is *not* here

A filled-in `compose.yml`. This repo is **public**; a real compose file carries the bind
address and the vault's path on the host. `compose.example.yml` is the placeholder version —
copy it out of the repo, fill it in there, and keep the filled copy with the private
deployment config. Keep it that way — see below.

The one line to be careful with is the port binding. `"<VPN_IP>:8080:8080"` publishes the site
to a single VPN address; shortening it to `"8080:8080"` binds `0.0.0.0` and exposes the vault
to the whole LAN. Docker writes its own iptables rules and bypasses `ufw`, so a host firewall
will not catch that mistake.

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

## Things that leak if enabled

- **`analytics:` — now `null`, and it must stay that way.** This entry previously read "no
  domain or key set today, so it's harmless." **That was wrong.** `provider: plausible` was
  inherited from upstream's default template and was live. It needs no configured domain: the
  emitter injects a script from `plausible.io` and sets `data-domain` from `location.hostname`
  at run time, then fires a `pageview` on every navigation. On a private vault that ships the
  host name and every note path visited to a third party. A *self-hosted* Plausible would be
  defensible; the default is not.
- `giscus` comments — disabled; enabling it embeds repository and category IDs.

The general lesson for this file: an unconfigured integration is not automatically an inert
one. Check what it does with no configuration before calling it harmless.
