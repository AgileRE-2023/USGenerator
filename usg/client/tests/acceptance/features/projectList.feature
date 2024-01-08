@order5
Feature: Project List
    Scenario: can see User Project From Login
    Given I am on SignIn Page
    When i fill in email field with usertesting461@gmail.com
    And i fill in password field with UserTesting123
    And i press SignIn button
    Then i should be on dashboard

    Scenario: can see User Project List from Input User Story User
    Given I am on SignIn Page
    When I press add project button on dashboard page
    Then The User should be on input user story page
    When I press User Story button
    Then i should be on dashboard again