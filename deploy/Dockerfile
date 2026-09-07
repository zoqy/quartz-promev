# promeV image for this fork.
#
# Deliberately NOT a modification of upstream's ./Dockerfile: keeping ours in deploy/ means
# `git merge upstream/v5` never conflicts over it. Build with:
#
#     docker build -f deploy/Dockerfile -t promev-quartz .
#
# Structure mirrors upstream's two-stage build so the dependency layer caches the same way.

FROM node:22-slim AS builder

# git is needed by `quartz plugin install`
RUN apt-get update \
 && apt-get install -y --no-install-recommends git ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package.json .
COPY package-lock.json* .
COPY .npmrc* .
COPY quartz/ ./quartz/
COPY quartz.lock.json* .
# `npm ci` rather than `npm install`: it installs exactly what package-lock.json pins and
# fails if the lock and package.json disagree, instead of quietly resolving new versions
# into the image. Every plugin here is an npm range (^0.1.0 and friends), so `npm install`
# in a fresh container can pick up releases the site was never checked against.
RUN npm ci && npx quartz plugin install

FROM node:22-slim

# git is needed at RUN TIME, not just to install plugins. The created-modified-date plugin
# resolves note dates from the vault's git history, and the vault is a bind mount that
# carries its own .git. Without git here the plugin logs "couldn't find git repository for
# content" and silently degrades to file mtimes, which on a bind mount are whatever the
# host last wrote rather than when the note was actually edited.
#
# `git config --global --add safe.directory` because the mount is owned by the host user,
# not by the container's, and git refuses to read a repository it considers foreign-owned.
RUN apt-get update \
 && apt-get install -y --no-install-recommends git ca-certificates \
 && rm -rf /var/lib/apt/lists/* \
 && git config --global --add safe.directory /app/content

WORKDIR /app
COPY --from=builder /app/ /app/
COPY . .

COPY deploy/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# The vault is bind-mounted read-only over this at run time. Cleared so the image can never
# carry note content, and so a missing mount fails visibly rather than serving stale files.
RUN rm -rf /app/content && mkdir -p /app/content

EXPOSE 8080 3001

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
