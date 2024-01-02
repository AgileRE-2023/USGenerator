Feature: User Story Scenario
    Scenario: User can generate user story scenario
        Given I am logged in as a user
        And I am in "Project List"
        When I press "add"
        Then I should see "Input User Story Page"
        When I fill in "User Stories Title" with "Instagram"
        And I fill in "Paragraf Description" with "Instagram is social media apps for knowing each other. As user can interact with others for sharing. You can post your photos and videos, so that others user can see. You can save photo from the others, so that you can see again that photo"
        And I press "Generate"
        Then I should see "User Stories List"
        When I press one of "user stories list"
        Then I should see "User Stories Scenario input page"
        When I fill in "User Stories Scneario Title" with "User can login home page"
        And I fill in "With a user who has successfully registered for the application and possesses valid credentials. When they initially open the application, they will be directed to the login screen. Here, they are prompted to input their previously registered username and password. After entering the credentials, the system will authenticate the provided information. If the entered credentials match those in the system, the user will gain access to the main interface of the application, enabling them to smoothly explore its features."
        And I press "Generate"
        Then I should see "User Stories Scenario List"
