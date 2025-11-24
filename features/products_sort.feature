Feature: Products sorting and validation
  Scenario: Sort products by price from Low to High
    Given I am logged in
    When I sort products by "Price (low to high)"
    Then the products should be sorted by price ascending

  Scenario: Sort products by price from High to Low
    Given I am logged in
    When I sort products by "Price (high to low)"
    Then the products should be sorted by price descending

  Scenario: Sort products by name from Z to A
    Given I am logged in
    When I sort products by "Name (Z to A)"
    Then the products should be sorted by name descending

  Scenario: Sort products by name from A to Z
    Given I am logged in
    When I sort products by "Name (A to Z)"
    Then the products should be sorted by name ascending