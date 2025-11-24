Feature: Shopping cart flow

Scenario: Verify products can be added and removed from the cart
    Given I am logged in
    When I add the first product to the cart
    Then the first product is added to the cart
    When I remove the first product from the cart
    Then the cart becomes empty