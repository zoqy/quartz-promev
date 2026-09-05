#!/bin/sh
# Runs at container start, before Quartz builds.
#
# Why this exists: baseUrl has to be in quartz.config.yaml at build time. Quartz v5 has no
# --baseUrl flag on `build` (it's on `create` only) and does no env-var substitution when
# loading config. But this repo is PUBLIC and the deployed baseUrl names a private tailnet
# host, so the real value cannot be committed. The committed value is the local-dev one and
# this rewrites it from the environment at start-up.
#
# Scope of a mistake here is small: baseUrl only affects absolute URLs - Open Graph tags, RSS
# and the sitemap. Internal links are relative, so a wrong or missing value yields bad social
# previews, not a broken site.
set -e

CONFIG=/app/quartz.config.yaml

if [ -n "${QUARTZ_BASE_URL:-}" ]; then
    # '|' as the delimiter because a URL contains '/'. Anchored to the two-space top-level
    # key so it cannot match a plugin option of the same name.
    sed -i "s|^  baseUrl:.*|  baseUrl: ${QUARTZ_BASE_URL}|" "$CONFIG"
    echo "[entrypoint] baseUrl -> ${QUARTZ_BASE_URL}"
else
    echo "[entrypoint] QUARTZ_BASE_URL unset; keeping committed default:"
    echo "[entrypoint]   $(grep '^  baseUrl:' "$CONFIG")"
    echo "[entrypoint] absolute URLs (OG tags, RSS, sitemap) will be wrong for this host."
fi

# --watch because the vault is a bind-mounted volume that changes underneath us; notes
# should appear without a rebuild.
exec npx quartz build --serve --watch --port 8080 --output public
