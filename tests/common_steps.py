from pytest_bdd import given
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# This is the commonly shared steps, including 'Given', 'When', 'Then', etc
@given('I am logged in')
def login_user(page):
    """
    Any scenarios have the step 'Given I am logged in' will execute this function
    """
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    # Assert it goes to the products page after login
    products_page = ProductsPage(page)
    products_page.assert_on_products_page()
