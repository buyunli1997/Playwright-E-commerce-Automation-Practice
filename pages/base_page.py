class BasePage:
    # Base page class of all pages where to write all common used methods
    def __init__(self, page):
        self.page = page

    def assert_text(self, locator, expected):
        text = self.page.locator(locator).text_content()
        assert expected in text, f"Expected '{expected}', got '{text}'"