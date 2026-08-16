# web4agent

Web reader CLIs built on [Camoufox](https://camoufox.com) (anti-detect Firefox).

## `murl` — markdown url

Fetch a webpage with Camoufox and print it as Markdown, curl-style:

```console
$ murl https://en.wikipedia.org/wiki/Markdown

# Markdown

| Markdown |  | 
|---|---|
| [Filename extensions](https://en.wikipedia.org/wiki/Filename_extension) | `.md` ,`.markdown` ... |
| [Internet media type](https://en.wikipedia.org/wiki/Media_type) | `text/markdown` ... |
...
```

Options:

- `--raw` — print raw HTML instead of extracted Markdown
- `--js JS` — run a JS function/expression in the page before extraction (repeatable)

If less than 200 chars can be extracted, `murl` warns and exits non-zero — try `--raw`.

## Install

```console
pip install web4agent
```

Python >= 3.10. Extraction is done by [trafilatura](https://trafilatura.readthedocs.io) in Markdown mode with links.

## License

MIT — see [LICENSE](LICENSE).
