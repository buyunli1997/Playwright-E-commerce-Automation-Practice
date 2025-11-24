from pages.base_page import BasePage


# This is the class to write all elements and actions in the products page
class ProductsPage(BasePage):
    TITLE = '.title'
    SORT_SELECT = '.product_sort_container'
    ITEMS = '.inventory_item'
    ADD_TO_CART_BTN = "//button[contains(.,'Add to cart')]"

    # Locators about the sorting feature
    ITEM_NAME = '.inventory_item_name'  # Product name

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

