from pages.base_page import BasePage

class ProductsPage(BasePage):

    TITLE = '.title'
    SORT_SELECT = '.product_sort_container'
    ITEMS = '.inventory_item'

    def assert_on_products_page(self):
        self.assert_text(self.TITLE, "Products")

    def select_sort(self, value):
        self.page.select_option(self.SORT_SELECT, value)

    def get_prices(self):
        locators = self.page.locator(".inventory_item_price")
        return [float(p.text_content().replace("$","")) for p in locators.all()]