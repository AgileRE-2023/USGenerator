@order1
Feature: Sign Up
    Scenario: Success SignUp
    Given i am on SignUp Page
    When i fill all field in SignUp Form with new username
    And i press SignUp button
    Then i should be on SignIn

    Scenario: Incomplete SignUp
    Given i am on SignUp Page
    When i fill in SignUp Form with incomplete data
    And i press SignUp button
    Then i should stay on SignUp 

