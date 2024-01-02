Feature: Register
    Scenario: User can make an account
        Given I am on register page
        When I fill in "Full Name" with "User Test"
        And I fill in "Email" with "usertesting461@gmail.com"
        And I fill in "Phone Number" with "088210973287"
        And I fill in "Password" with "UserTesting123"
        And I fill in "Confirm Password" with "UserTesting123"
        And I press Sign Up button
        Then I should see "Login Page"