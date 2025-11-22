Feature: Shopping cart flow

  Scenario: Add item to card
    Given I am logged in
    When I add the first item
    Then I should see the item in the cart