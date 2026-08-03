from playwright.sync_api import Page, expect
from config import BASE_URL

DROPDOWN_URL = f"{BASE_URL}/dropdown"

def test_dropdown_default_state(page: Page):
    """Test that dropdown loads with the default placeholder option"""
    page.goto(DROPDOWN_URL)

    dropdown = page.locator("#dropdown")
    expect(dropdown).to_be_visible()

    # Default selected value should be empty (placeholder "Please select an option")
    default_value = dropdown.input_value()
    assert default_value == "", \
        f"Expected empty default value, got: '{default_value}'"

def test_dropdown_select_by_value(page: Page):
    """Test selecting Option 1 by its value attribute"""
    page.goto(DROPDOWN_URL)


    dropdown = page.locator("#dropdown")

    # Select by value attribute
    dropdown.select_option("1")

    # Verify via input_value
    assert dropdown.input_value() == "1", \
        "Expected value '1' after selecting Option 1"

    # Verify via expect
    expect(dropdown).to_have_value("1")

def test_dropdown_select_by_label(page: Page):
    """Test selecting Option 2 by its visible text label"""
    page.goto(DROPDOWN_URL)

    dropdown = page.locator("#dropdown")

    # Select by visible text
    dropdown.select_option(label="Option 2")

    # Verify via input_value
    assert dropdown.input_value() == "2", \
        "Expected value '2' after selecting Option 2"

    # Verify via expect
    expect(dropdown).to_have_value("2")

def test_dropdown_switch_between_options(page: Page):
    """Test switching from Option 1 to Option 2"""
    page.goto(DROPDOWN_URL)

    dropdown = page.locator("#dropdown")

    # Select Option 1 first
    dropdown.select_option("1")
    expect(dropdown).to_have_value("1")

    # Switch to Option 2
    dropdown.select_option("2")
    expect(dropdown).to_have_value("2")

    assert dropdown.input_value() == "2", \
        "Expected value '2' after switching from Option 1 to Option 2"