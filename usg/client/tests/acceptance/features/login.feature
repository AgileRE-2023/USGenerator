Feature: Login
    Scenario: User can login into project list page
        Given I am on login page
        When I fill in "Email" with "usertesting461@gmail.com"
        And I fill in "Password" with "UserTesting123"
        And I press "Login Button"
        Then I should see "Project List Page"