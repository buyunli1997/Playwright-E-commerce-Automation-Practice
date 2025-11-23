Feature: Shopping cart flow

  Scenario: Add item to cart
    Given I am logged in
    When I add the first product to the cart
    Then I should see at least 1 item in the cart