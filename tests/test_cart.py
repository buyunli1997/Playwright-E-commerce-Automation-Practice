from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_add_to_cart(page):
    # login
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    products_page.assert_on_products_page()

    # add the first item
    page.click("(//button[contains(.,'Add to cart')])[1]")

    cart_page = CartPage(page)
    cart_page.open_cart()

    items = cart_page.get_item_names()

    assert len(items) >= 1, "Cart is empty!"