@order6
Feature: User Profile
    Scenario: Can edit user profile page
    Given As a logged user
    When I press profile icon
    Then I should see user profile page
    When I press edit profile button
    Then I should see edit profile page
    When I fill all field in edit profile form with new data
    And I press save change button
    Then I should see user profile page again

