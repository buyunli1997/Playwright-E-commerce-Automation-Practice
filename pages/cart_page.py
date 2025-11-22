from pages.base_page import BasePage

class CartPage(BasePage):

    ITEM_NAME = ".inventory_item_name"
    CART_LINK = ".shopping_cart_link"

    def open_cart(self):
        self.page.click(self.CART_LINK)

    def get_item_names(self):
        return [i.text_content() for i in self.page.locator(self.CART_LINK).all()]