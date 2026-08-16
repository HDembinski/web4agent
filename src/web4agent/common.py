"""Shared fetch helper: headless Camoufox page."""
from contextlib import contextmanager

from camoufox.sync_api import Camoufox


@contextmanager
def camoufox_page(url: str):
    """Open url in headless Camoufox and yield the live playwright page."""
    with Camoufox(headless=True) as browser:
        page = browser.new_page()
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(1000)  # let late JS / lazy content settle
        yield page
