@order2
Feature: Sign In
    Scenario: Success SignIn
    Given i am on SignIn Page
    When i fill in email field with usertesting461@gmail.com
    And i fill in password field with UserTesting123
    And i press SignIn button
    Then i should be on dashboard

    Scenario: Incorrect username or Password
    Given i am on SignIn Page
    When i fill in email field with usertesting461@gmail.com
    And i fill in password field with UserTesting12
    And i press SignIn button
    Then i should stay on SignIn