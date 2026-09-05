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
RUN npm install && npx quartz plugin install

FROM node:22-slim
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
