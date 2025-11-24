import pytest
from pytest_bdd import scenario, when, then, parsers
from pages.products_page import ProductsPage
# make sure pytest_bdd can find 'Given I am logged in'
from tests import common_steps


@scenario('../features/products_sort.feature', 'Sort products by price from Low to High')
def test_sort_price_low_to_high():
    pass


@scenario('../features/products_sort.feature', 'Sort products by price from High to Low')
def test_sort_price_high_to_low():
    pass


@scenario('../features/products_sort.feature', 'Sort products by name from Z to A')
def test_sort_name_z_to_a():
    pass


@scenario('../features/products_sort.feature', 'Sort products by name from A to Z')
def test_sort_name_a_to_z():
    pass


# 'Given' is in common_steps.py and imported
@when(parsers.parse('I sort products by "{sort_order}"'))
def sort_products(page, sort_order):
    # :param sort_order: Price (low to high), Price (high to low), Name (A to Z), Name (Z to A),
    products_page = ProductsPage(page)
    products_page.select_sort(sort_order)


# 'Then' Steps
@then('the products should be sorted by price ascending')
def check_price_ascending(page):
    products_page = ProductsPage(page)
    actual_prices = products_page.get_prices()

    # Use sorted()to create the expected ascending price list for assertion
    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices, \
        f"Price is not ascending.Expected: {expected_prices}, Actual: {actual_prices}"


@then('the products should be sorted by price descending')
def check_price_descending(page):
    products_page = ProductsPage(page)
    actual_prices = products_page.get_prices()

    # Use sorted() and make reverse=True to create descending price list for assertion
    expected_prices = sorted(actual_prices, reverse=True)

    assert actual_prices == expected_prices, \
        f"Price is not descending, expected： {expected_prices}, actual: {actual_prices}"


@then('the products should be sorted by name descending')
def check_name_descending(page):
    products_page = ProductsPage(page)
    actual_names = products_page.get_names()

    # Use sorted() and make reverse=True to created the Z to A sorting list for assertion
    expected_names = sorted(actual_names, reverse=True)

    assert actual_names == expected_names, \
        f"Name is not from Z to A. Expected:{expected_names}, Actual: {actual_names}"


@then('the products should be sorted by name ascending')
def check_name_ascending(page):
    products_page = ProductsPage(page)
    actual_names = products_page.get_names()

    # Use sorted() to create the expected A to Z sorting list for assertion
    expected_names = sorted(actual_names)

    assert actual_names == expected_names, \
        f"Name is not from A to Z. Expected: {expected_names}, Actual: {actual_names}"