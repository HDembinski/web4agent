# web4agent

Web reader CLIs built on [Camoufox](https://camoufox.com) (anti-detect Firefox).

## `murl` — markdown url

Fetch a webpage with Camoufox and print it as Markdown, curl-style:

```console
$ murl https://example.com

# Example Domain

<url>https://example.com</url>

---
title: Example Domain
url: https://example.com
hostname: example.com
sitename: example.com
---
This domain is for use in documentation examples without needing permission. Avoid use in operations.

Learn more
```

Options:

- `--raw` — print raw HTML instead of extracted Markdown
- `--js JS` — run a JS function/expression in the page before extraction (repeatable)

If less than 200 chars can be extracted, `murl` warns and exits non-zero — try `--raw`.

## Install

```console
pip install web4agent
```

Python >= 3.10. Extraction is done by [trafilatura](https://trafilatura.readthedocs.io) in Markdown mode with links and metadata.

## License

MIT — see [LICENSE](LICENSE).
