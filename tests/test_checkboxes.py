from playwright.sync_api import Page, expect
from config import BASE_URL

CHECKBOXES_URL = f"{BASE_URL}/checkboxes"

def test_check_checkbox(page: Page):
    """Test checking the first checkbox (initially unchecked)"""
    page.goto(CHECKBOXES_URL)

    # First checkbox is unchecked by default on this page
    checkbox1 = page.locator("input[type='checkbox']").first

    # Verify initial state – unchecked
    assert not checkbox1.is_checked(), \
        "Checkbox 1 should be unchecked by default"

    # Check it
    checkbox1.check()

    # Verify it's now checked
    assert checkbox1.is_checked(), \
        "Checkbox 1 should be checked after .check()"

    # Extra: Playwright expect for sure
    expect(checkbox1).to_be_checked()

def test_uncheck_checkbox(page: Page):
    """Test unchecking the second checkbox (initially checked)"""
    page.goto(CHECKBOXES_URL)

    # Second checkbox is checked by default on this page
    checkbox2 = page.locator("input[type='checkbox']").nth(1)

    # Verify initial state – checked
    assert checkbox2.is_checked(), \
        "Checkbox 2 should be checked by default"

    # Uncheck it
    checkbox2.uncheck()

    # Verify it's now unchecked
    assert not checkbox2.is_checked(), \
        "Checkbox 2 should be unchecked after .uncheck()"

    # Extra: Playwright expect pro jistotu
    expect(checkbox2).not_to_be_checked()

def test_toggle_both_checkboxes(page: Page):
    """Test toggling both checkboxes and verifying final state"""
    page.goto(CHECKBOXES_URL)

    checkbox1 = page.locator("input[type='checkbox']").first
    checkbox2 = page.locator("input[type='checkbox']").nth(1)

    # Check checkbox1, uncheck checkbox2
    checkbox1.check()
    checkbox2.uncheck()

    # Verify final states
    expect(checkbox1).to_be_checked()
    expect(checkbox2).not_to_be_checked()