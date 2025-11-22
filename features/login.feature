Feature: Login authentication

  Scenario: Valid user can login successfully
    Given I open the login page
    When I login with "standard_user" and "secret_sauce"
    Then I should see the products page

  Scenario: Invalid user sees error message
    Given I open the login page
    When I login with "wrong_user" and "wrong_pass"
    Then I should see login error "Epic sadface"