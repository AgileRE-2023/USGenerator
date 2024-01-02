Feature: User Story
    Scenario: User can generate user story
        Given I am logged in as a user
        And I am in "Project List"
        When I press "add"
        Then I should see "Input User Story Page"
        When I fill in "User Stories Title" with "Instagram"
        And I fill in "Paragraf Description" with "Instagram is social media apps for knowing each other. As user can interact with others for sharing. You can post your photos and videos, so that others user can see. You can save photo from the others, so that you can see again that photo"
        And I press "Generate"
        Then I should see "User Stories List"