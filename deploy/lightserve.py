#!/usr/bin/env python3
"""Serve an already-built Quartz site with a tiny memory footprint.

Why this exists: `npx quartz build --serve --watch` runs esbuild and a file watcher and sits
around 250-500 MB. On a machine under memory pressure it gets OOM-killed mid-session, which
drops the page out from under whoever is reading it on a phone. This serves the finished
`public/` directory instead, in a few MB, with no watcher.

The catch it handles: Quartz emits `topics/foo.html` but links to `/topics/foo`. A stock
`http.server` returns 404 for those, so this retries with `.html` and with `/index.html`.

    python deploy/lightserve.py [port] [directory]

No rebuild happens here. After changing styles or notes, run a one-off build:
    npx quartz build --output public
"""
import functools
import http.server
import os
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
ROOT = sys.argv[2] if len(sys.argv) > 2 else "public"


class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        local = super().translate_path(path)
        if os.path.isdir(local):
            index = os.path.join(local, "index.html")
            if os.path.exists(index):
                return index
        if not os.path.exists(local):
            for candidate in (local + ".html", os.path.join(local, "index.html")):
                if os.path.exists(candidate):
                    return candidate
        return local

    def end_headers(self):
        # a dev server should never have a stale stylesheet cached on a phone
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.address_string(), fmt % args))


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if not os.path.isdir(ROOT):
    sys.exit(f"no such directory: {ROOT!r} - build first with: npx quartz build --output public")

handler = functools.partial(CleanUrlHandler, directory=ROOT)
# "" binds all interfaces, so the phone can reach it over the LAN or the tailnet.
with Server(("", PORT), handler) as httpd:
    print(f"serving {os.path.abspath(ROOT)} on port {PORT} (all interfaces)", flush=True)
    httpd.serve_forever()
