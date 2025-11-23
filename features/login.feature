Feature: Login authentication

  Scenario Outline: Valid user can login successfully
    Given I open the login page
    When I login with "<username>" and "<password>"
    Then I should see the products page
    Examples: Valid Credentials
  | username                 | password        |
  | standard_user            | secret_sauce    |
  | problem_user             | secret_sauce    |
  | performance_glitch_user  | secret_sauce    |


  Scenario: Invalid user sees error message
    Given I open the login page
    When I login with "wrong_user" and "wrong_pass"
    Then I should see login error "Epic sadface"