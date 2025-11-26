from pytest_bdd import scenario, when, then
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from tests import common_steps


@scenario('../features/cart.feature', 'Verify products can be added and removed from the cart')
def test_add_to_and_remove_from_cart(page):
    # Actions are defined in the following functions
    pass

# @given("I am logged in")' step is in common_steps.py
@when('I add the first product to the cart')
def add_first_item(page):
    products_page = ProductsPage(page)
    products_page.assert_on_products_page()
    products_page.add_first_item_to_cart()


@then('the first product is added to the cart')
def check_cart_count(page):
    cart_page = CartPage(page)
    cart_page.open_cart()
    # Check if the cart is empty
    items = cart_page.get_item_names()
    assert len(items) == 1, "Cart is empty!"


@when('I remove the first product from the cart')
def remove_first_item(page):
    cart_page = CartPage(page)
    cart_page.open_cart()
    cart_page.delete_first_item_from_cart()


@then('the cart becomes empty')
def check_empty_cart_count(page):
    cart_page = CartPage(page)
    cart_page.open_cart()
    # Check if the cart is empty
    items = cart_page.get_item_names()
    assert len(items) == 0, "Cart is not empty!"
