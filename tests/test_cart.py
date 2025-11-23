from pytest_bdd import scenario, when, then
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from tests import common_steps


@scenario('../features/cart.feature', 'Add item to cart')
def test_add_to_cart(page):
    # Actions are defined in the following functions
    pass

# @given("I am logged in")' step is in common_steps.py
@when('I add the first product to the cart')
def add_first_item(page):
    products_page = ProductsPage(page)
    products_page.assert_on_products_page()
    products_page.add_first_item_to_cart()


@then('I should see at least 1 item in the cart')
def check_cart_count(page):
    cart_page = CartPage(page)
    cart_page.open_cart()
    # Check if the cart is empty
    items = cart_page.get_item_names()
    assert len(items) >= 1, "Cart is empty!"