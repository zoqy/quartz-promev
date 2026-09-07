> **This is a fork.** It publishes one private Obsidian vault as a self-hosted site reachable
> only over a VPN. Upstream's own README follows below, unchanged.
>
> **Read [`deploy/README.md`](deploy/README.md) before deploying or changing config.** Two
> things here are dangerous to get wrong and both are explained there:
>
> - **The port binding is a security boundary.** `"<VPN_IP>:8080:8080"` keeps the vault on the
>   VPN. Shortening it to `"8080:8080"` publishes private notes to the whole LAN, and Docker
>   bypasses `ufw`, so no host firewall catches it.
> - **`analytics:` must stay `null`.** Upstream's default template enables Plausible, which
>   needs no configuration to start reporting the hostname and every visited note path to a
>   third party.
>
> What is deliberately *not* here: a filled-in compose file. This repo is public and a real one
> names the bind address and the vault's path on the host. Copy `deploy/compose.example.yml`
> and fill it in outside the repo.
>
> Divergence from upstream is confined to `deploy/`, `quartz.config.yaml`,
> `quartz/styles/custom.scss`, `quartz/static/`, and the fixture vault in `content/`, so
> `git fetch upstream && git merge upstream/v5` stays cheap.

---

# Quartz v5

> “[One] who works with the door open gets all kinds of interruptions, but [they] also occasionally gets clues as to what the world is and what might be important.” — Richard Hamming

Quartz is a set of tools that helps you publish your [digital garden](https://jzhao.xyz/posts/networked-thought) and notes as a website for free.

🔗 Read the documentation and get started: https://quartz.jzhao.xyz/

[Join the Discord Community](https://discord.gg/cRFFHYye7t)

## Sponsors

<p align="center">
  <a href="https://github.com/sponsors/jackyzha0">
    <img src="https://cdn.jsdelivr.net/gh/jackyzha0/jackyzha0/sponsorkit/sponsors.svg" />
  </a>
</p>
