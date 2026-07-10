from playwright.sync_api import Page
from config import BASE_URL

def test_add_element(page: Page):
    """Test adding an element shows Delete button"""
    page.goto(f"{BASE_URL}/add_remove_elements/")

    # Click Add Element
    page.locator("button", has_text="Add Element").click()

    # Verify one Delete button is visible
    delete_buttons = page.locator("button", has_text="Delete")
    assert delete_buttons.count() == 1, "Expected 1 Delete button after adding element"

def test_remove_element(page: Page):
    """Test removing an added element hides Delete button"""
    page.goto(f"{BASE_URL}/add_remove_elements/")

    # Add element first
    page.locator("button", has_text="Add Element").click()

    # Remove it
    page.locator("button", has_text="Delete").click()

    # Verify Delete button is gone
    delete_buttons = page.locator("button", has_text="Delete")
    assert delete_buttons.count() == 0, "Expected 0 Delete buttons after removing element"