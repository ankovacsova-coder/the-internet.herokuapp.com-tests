from playwright.sync_api import Page


def test_check_checkbox(page: Page):
    """Test checking and unchecking checkboxes"""
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # Find the first checkbox
    checkbox1 = page.locator("input[type='checkbox']").first

    # Check if it's unchecked
    assert not checkbox1.is_checked()

    # Check it
    checkbox1.check()

    # Verify it's now checked
    assert checkbox1.is_checked()

    print("Checkbox test passed")



def test_uncheck_checkbox(page: Page):
    """Test unchecking a pre-checked checkbox"""
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # Find the second checkbox (already checked)
    checkbox2 = page.locator("input[type='checkbox']").nth(1)

    # Verify it's checked
    assert checkbox2.is_checked()

    # Uncheck it
    checkbox2.uncheck()

    # Verify it's now unchecked
    assert not checkbox2.is_checked()

    print("Uncheck test passed")