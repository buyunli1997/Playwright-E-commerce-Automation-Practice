from pytest_bdd import scenario, when, then, parsers
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from tests import common_steps


@scenario('../features/checkout.feature', 'Successful purchase of two items')
def test_successful_checkout(page):
    pass


# @Given() can be found through "from tests import common_steps"
@when('I add two different products to the cart')
def add_two_items(page):
    products_page = ProductsPage(page)
    products_page.add_first_item_to_cart()
    products_page.add_second_item_to_cart()


@when('I navigate to the cart page')
def navigate_to_cart(page):
    cart_page = CartPage(page)
    cart_page.open_cart()


@when('I click the "Checkout" button')
def click_checkout_button(page):
    checkout_page = CheckoutPage(page)
    checkout_page.click_checkout()


@when(parsers.parse('I fill out the shipping information with "{first_name}", "{last_name}" and "{zip_code}"'))
def fill_out_info(page, first_name, last_name, zip_code):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_shipping_info(first_name, last_name, zip_code)


@when('I click the "Continue" button')
def click_continue_button(page):
    checkout_page = CheckoutPage(page)
    checkout_page.click_continue()


@when('I click the "Finish" button')
def click_finish_button(page):
    checkout_page = CheckoutPage(page)
    checkout_page.click_finish()


@then('the subtotal price should be calculated correctly')
def check_subtotal_price(page):
    checkout_page = CheckoutPage(page)
    actual_subtotal = checkout_page.get_actual_subtotal()
    expected_subtotal = checkout_page.get_expected_subtotal()

    assert actual_subtotal == expected_subtotal, \
        f"Subtotal is incorrect. Expected: ${expected_subtotal}, Actual: ${actual_subtotal}"


@then('the total price should be calculated correctly')
def check_total_price(page):
    checkout_page = CheckoutPage(page)
    expected_subtotal = checkout_page.get_expected_subtotal()
    # actual_subtotal = checkout_page.get_actual_subtotal()
    actual_tax = checkout_page.get_tax()
    actual_total = checkout_page.get_actual_total()
    expected_total = round(expected_subtotal + actual_tax, 2)

    assert actual_total == expected_total, \
        f"Total price is incorrect. Expected: ${expected_total} (Subtotal + Tax), Actual: ${actual_total}"


@then(parsers.parse('I should see the checkout complete message "{expected_message}"'))
def check_checkout_complete(page, expected_message):
    checkout_page = CheckoutPage(page)
    actual_message = checkout_page.get_complete_message()

    assert actual_message == expected_message, \
        f"Checkout complete message is incorrect. Expected: '{expected_message}', Actual: '{actual_message}'"