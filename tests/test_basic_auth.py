from playwright.sync_api import Page, expect
from config import BASE_URL, BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD

BASIC_AUTH_URL = f"{BASE_URL}/basic_auth"

def test_basic_auth_success(page: Page):
    """Test successful basic authentication with valid credentials"""
    # Navigate with credentials embedded in URL
    authenticated_url = f"https://{BASIC_AUTH_USERNAME}:{BASIC_AUTH_PASSWORD}@the-internet.herokuapp.com/basic_auth"
    page.goto(authenticated_url)

    # Verify successful authentication message
    content = page.locator(".example p")
    expect(content).to_be_visible()
    expect(content).to_contain_text("Congratulations")

    # Verify heading
    heading = page.locator("h3")
    expect(heading).to_be_visible()
    expect(heading).to_have_text("Basic Auth")

def test_basic_auth_page_structure(page: Page):
    """Test that the basic auth page has expected structure after authentication"""
    authenticated_url = f"https://{BASIC_AUTH_USERNAME}:{BASIC_AUTH_PASSWORD}@the-internet.herokuapp.com/basic_auth"
    page.goto(authenticated_url)

    # Verify page elements exist
    example_div = page.locator(".example")
    expect(example_div).to_be_visible()

    # Verify success message content
    success_message = page.locator(".example p").inner_text()
    assert "Congratulations" in success_message, \
        f"Expected success message to contain 'Congratulations', got: '{success_message}'"
    assert "proper credentials" in success_message.lower(), \
        f"Expected success message to mention 'proper credentials', got: '{success_message}'"