import re
from playwright.sync_api import Page, expect
from config import BASE_URL

AB_URL = f"{BASE_URL}/abtest"
VALID_VARIATIONS = ["A/B Test Control", "A/B Test Variation 1"]

def test_ab_testing_page_loads(page: Page):
    """Test that the A/B Testing page loads correctly"""
    page.goto(AB_URL)

    # Verify heading is visible
    heading = page.locator("h3")
    expect(heading).to_be_visible()

    # Heading must be one of the valid variations
    heading_text = heading.inner_text()
    assert heading_text in VALID_VARIATIONS, \
        f"Unexpected heading: '{heading_text}'. Expected one of: {VALID_VARIATIONS}"

def test_ab_testing_content_exists(page: Page):
    """Test that the A/B Testing page contains expected content"""
    page.goto(AB_URL)

    # Verify paragraph content is visible and not empty
    content = page.locator(".example p")
    expect(content).to_be_visible()

    content_text = content.inner_text()
    assert len(content_text) > 0, "Page content should not be empty"

def test_ab_testing_opt_out_link(page: Page):
    """Test that the opt-out link works correctly"""
    page.goto(AB_URL)

    # Get initial heading
    heading = page.locator("h3")
    initial_heading = heading.inner_text()

    # Check if opt-out link exists
    opt_out_link = page.locator("a[href*='abtest']")

    if opt_out_link.count() > 0:
        opt_out_link.first.click()

        # Verify we stayed on abtest page (flexible URL match)
        expect(page).to_have_url(re.compile(r".*/abtest.*"))

        after_heading = page.locator("h3").inner_text()
        assert after_heading in VALID_VARIATIONS, \
            f"After opt-out: unexpected heading '{after_heading}'"

def test_ab_testing_variations(page: Page):
    """Test that A/B Testing shows one of the expected variations"""
    page.goto(AB_URL)

    # Verify heading is one of valid variations
    heading = page.locator("h3")
    expect(heading).to_be_visible()

    heading_text = heading.inner_text()
    assert heading_text in VALID_VARIATIONS, \
        f"Expected one of {VALID_VARIATIONS}, but got '{heading_text}'"

    # Verify overall page structure exists
    example_div = page.locator(".example")
    expect(example_div).to_be_visible()