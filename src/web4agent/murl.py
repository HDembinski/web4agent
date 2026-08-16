"""murl — markdown url. Fetch a webpage with Camoufox and print it as Markdown (curl-like)."""
import argparse
import re
import sys

from .common import camoufox_page


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Fetch a webpage with Camoufox (anti-detect Firefox) and print it as Markdown."
    )
    ap.add_argument("url")
    ap.add_argument("--raw", action="store_true", help="print raw HTML instead of extracted Markdown")
    ap.add_argument("--js", action="append", metavar="JS",
                    help="JS function/expression to run in the page before extraction (repeatable)")
    args = ap.parse_args()

    with camoufox_page(args.url) as page:
        for js in args.js or []:
            page.evaluate(js)  # DOM mutations are picked up by page.content()
        title = (page.title() or "").strip()
        html = page.content()

    if args.raw:
        print(html)
        return

    import trafilatura  # lazy: --raw and arg parsing stay fast

    text = (
        trafilatura.extract(
            html,
            url=args.url,
            output_format="markdown",
            favor_recall=True,  # less aggressive filtering than the precision default
            include_links=True,
            with_metadata=True,
        )
        or ""
    ).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)

    if len(text) < 200:
        print(
            f"[murl] only {len(text)} chars extractable from {args.url} (title: {title!r}) — try --raw",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"# {title or args.url}\n\n<url>{args.url}</url>\n\n{text}")
