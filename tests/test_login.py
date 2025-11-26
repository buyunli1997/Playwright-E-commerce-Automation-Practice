import pytest
from pytest_bdd import scenario, given, parsers, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.data_driven
@pytest.mark.critical
@pytest.mark.regression
@scenario('../features/login.feature', 'Valid user can login successfully')
def test_valid_login(page):
    pass
    # login_page = LoginPage(page)
    # login_page.login("standard_user", "secret_sauce")
    #
    # products_page = ProductsPage(page)
    # products_page.assert_on_products_page()


@pytest.mark.smoke
@pytest.mark.critical
@pytest.mark.regression
@scenario('../features/login.feature', 'Invalid user sees error message')
def test_invalid_login(page):
    pass
    # login_page = LoginPage(page)
    # login_page.login("wrong_user", "wrong_pass")
    # login_page.assert_login_error("Epic sadface")


# Shared Steps @given（'I open the login page'）
@given('I open the login page')
def open_login_page(page):
    # The page fixture handles opening the base URL (login page).
    # Because the page fixture in conftest.py has already navigated to https://www.saucedemo.com/, this function only need to make sure the page object is useable.
    pass


@when(parsers.parse('I login with "{username}" and "{password}"'))
def login_with_credentials(page, username, password):
    login_page = LoginPage(page)
    login_page.login(username, password)


@then('I should see the products page')
def check_products_page(page):
    # Asserts that the user is successfully redirected to the products page.
    products_page = ProductsPage(page)
    products_page.assert_on_products_page()


@then(parsers.parse('I should see login error "{error_msg}"'))
def check_login_error(page, error_msg):
    # Asserts that the expected login error message is displayed.
    login_page = LoginPage(page)
    login_page.assert_login_error(error_msg)