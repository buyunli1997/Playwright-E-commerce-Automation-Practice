Feature: Checkout and purchase flow

  @smoke
  @critical
  @regression
  Scenario: Successful purchase of two items
    Given I am logged in
    When I add two different products to the cart
    And I navigate to the cart page
    And I click the "Checkout" button
    And I fill out the shipping information with "John", "Doe" and "90210"
    And I click the "Continue" button
    Then the subtotal price should be calculated correctly
    And the total price should be calculated correctly
    When I click the "Finish" button
    Then I should see the checkout complete message "Thank you for your order!"