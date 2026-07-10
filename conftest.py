import pytest
from playwright.sync_api import sync_playwright
from config import BROWSER, HEADLESS, SLOW_MO

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = getattr(p, BROWSER).launch(
            headless=HEADLESS,
            slow_mo=SLOW_MO
        )
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()