from playwright.sync_api import Page, expect


def test_ab_testing_page_loads(page: Page):
    """Test that the A/B Testing page loads correctly"""
    page.goto("https://the-internet.herokuapp.com/abtest")

    # Verify the page has loaded by checking for the heading
    heading = page.locator("h3")
    expect(heading).to_be_visible()

    # The heading should be either "A/B Test Control" or "A/B Test Variation 1"
    heading_text = heading.inner_text()
    assert heading_text in ["A/B Test Control", "A/B Test Variation 1"], \
        f"Unexpected heading: {heading_text}"

    print(f"A/B Testing page loaded with heading: {heading_text}")


def test_ab_testing_content_exists(page: Page):
    """Test that the A/B Testing page contains expected content"""
    page.goto("https://the-internet.herokuapp.com/abtest")

    # Verify the page content is present
    content = page.locator(".example p")
    expect(content).to_be_visible()

    # Verify that content is not empty
    content_text = content.inner_text()
    assert len(content_text) > 0, "Content should not be empty"

    print("A/B Testing page content verified")


def test_ab_testing_opt_out_link(page: Page):
    """Test that the opt-out link works correctly"""
    page.goto("https://the-internet.herokuapp.com/abtest")

    # Get the initial heading
    heading = page.locator("h3")
    initial_heading = heading.inner_text()

    # Check if opt-out link exists
    opt_out_link = page.locator("a[href*='abtest']")

    if opt_out_link.count() > 0:
        opt_out_link.first.click()

        # Verify we're still on an abtest page
        expect(page).to_have_url("https://the-internet.herokuapp.com/abtest")

        print(f"Started with: {initial_heading}, navigated via opt-out link")
    else:
        print("No opt-out link found on this variation")


def test_ab_testing_variations(page: Page):
    """Test that A/B Testing shows one of the expected variations"""
    page.goto("https://the-internet.herokuapp.com/abtest")

    # Check the heading
    heading = page.locator("h3")
    expect(heading).to_be_visible()
    heading_text = heading.inner_text()

    # Verify it's one of the valid variations
    valid_variations = ["A/B Test Control", "A/B Test Variation 1"]
    assert heading_text in valid_variations, \
        f"Expected one of {valid_variations}, but got '{heading_text}'"

    # Verify the page structure
    example_div = page.locator(".example")
    expect(example_div).to_be_visible()

    print(f"A/B Testing variation detected: {heading_text}")

