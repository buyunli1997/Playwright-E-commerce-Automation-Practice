from pages.base_page import BasePage


# This is the class to write all elements and actions in the products page
class ProductsPage(BasePage):
    TITLE = '.title'
    SORT_SELECT = '.product_sort_container'
    ITEMS = '.inventory_item'
    ADD_TO_CART_BTN = "//button[contains(.,'Add to cart')]"

    # Locators about the sorting feature
    ITEM_NAME = '.inventory_item_name'  # Product name

    # Used for verifying button state and removing from list
    FIRST_PRODUCT_BUTTON = '.inventory_item:nth-child(1) button'

    # Used for multi-item tests
    SECOND_PRODUCT_ADD_BTN = "button[data-test='add-to-cart-sauce-labs-bike-light']"

    # Used for navigating to detail page
    FIRST_PRODUCT_LINK = '#item_4_title_link'

    # Assert the current page is the products page
    def assert_on_products_page(self):
        self.assert_text(self.TITLE, "Products")

    # Select the sort option through the drop-down list
    def select_sort(self, value):
        self.page.select_option(self.SORT_SELECT, value)

    # Get the price of all items
    def get_prices(self):
        locators = self.page.locator(".inventory_item_price")
        return [float(p.text_content().replace("$","")) for p in locators.all()]

    # Get names of all products
    def get_names(self):
        locators = self.page.locator(self.ITEM_NAME)
        return [name.text_content() for name in locators.all()]

    # Add an item to the cart
    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).first.click()

    # Add the second item to the cart
    def add_second_item_to_cart(self):
        self.page.click(self.SECOND_PRODUCT_ADD_BTN)

    # Remove the first product from the cart
    def remove_first_item_from_list(self):
        self.page.locator(self.FIRST_PRODUCT_BUTTON).click()
