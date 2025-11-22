import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    products_page.assert_on_products_page()

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.login("wrong_user", "wrong_pass")

    login_page.assert_login_error("Epic sadface")