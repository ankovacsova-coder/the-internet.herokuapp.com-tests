from playwright.sync_api import Page


def test_dropdown_selection(page: Page):
    """Test selecting options from a dropdown menu"""
    page.goto("https://the-internet.herokuapp.com/dropdown")

    # Locate the dropdown element
    dropdown = page.locator("#dropdown")

    # Select option by value
    dropdown.select_option("1")

    # Verify the selection
    assert dropdown.input_value() == "1"

    # Select option by text
    dropdown.select_option(label="Option 2")

    # Verify the selection
    assert dropdown.input_value() == "2"


    print("Dropdown test passed")