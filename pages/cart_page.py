from pages.base_page import BasePage


# The class to write all elements and actions in the cart page
class CartPage(BasePage):
    ITEM_NAME = ".inventory_item_name"
    CART_LINK = ".shopping_cart_link"

    # Enter the shopping cart
    def open_cart(self):
        self.page.click(self.CART_LINK)

    # Get the names of all items in the shopping cart
    def get_item_names(self):
        return [i.text_content() for i in self.page.locator(self.ITEM_NAME).all()]