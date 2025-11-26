from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Locators for Checkout Step One (Shipping Information)
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP_CODE = "#postal-code"
    CONTINUE_BTN = "#continue"

    PRICE = "[data-test = 'inventory-item-price']"

    # Locators for Checkout Step Two (Overview)
    SUBTOTAL_PRICE = ".summary_subtotal_label"
    TAX_PRICE = ".summary_tax_label"
    TOTAL_PRICE = ".summary_total_label"
    FINISH_BTN = "#finish"

    # Locators for Checkout Complete
    COMPLETE_HEADER = ".complete-header"

    # Locators for buttons shared with CartPage
    CHECKOUT_BTN = "#checkout"

    # Fill shipping info
    def fill_shipping_info(self, first_name, last_name, zip_code):
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.ZIP_CODE, zip_code)

    # Click the Continue button
    def click_continue(self):
        self.page.locator(self.CONTINUE_BTN).click()

    # Click the Finish button
    def click_finish(self):
        self.page.locator(self.FINISH_BTN).click()

    # Click the Checkout button
    def click_checkout(self):
        self.page.locator(self.CHECKOUT_BTN).click()

    # Shared function to get diff prices, subtotal, tax
    def _get_price_value(self, locator_object):
        """Helper to extract float price from text like 'Subtotal: $29.99'"""
        text = locator_object.text_content()
        # Find the dollar sign, and replace it and any prefix text before the number
        return float(text.split('$')[-1])

    # Get the expected subtotal price
    def get_expected_subtotal(self):
        price_1 = self._get_price_value(self.page.locator(self.PRICE).first)
        price_2 = self._get_price_value(self.page.locator(self.PRICE).last)
        return round(price_1 + price_2, 2)

    # Get the actual subtotal price
    def get_actual_subtotal(self):
        subtotal_locator = self.page.locator(self.SUBTOTAL_PRICE)
        return self._get_price_value(subtotal_locator)

    # Get the tax value
    def get_tax(self):
        tax_locator = self.page.locator(self.TAX_PRICE)
        return self._get_price_value(tax_locator)

    # Get the total price
    def get_actual_total(self):
        subtotal_locator = self.page.locator(self.TOTAL_PRICE)
        return self._get_price_value(subtotal_locator)

    # Get the message after the order is submitted
    def get_complete_message(self):
        complete_message = self.page.locator(self.COMPLETE_HEADER).text_content()
        return complete_message
