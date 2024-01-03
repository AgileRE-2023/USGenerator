@order4
Feature: User Story
    Scenario: Input Apps Desc
    Given i am on User Stories Page
    When I press one of an user stories
    Then i should be on input user story Scenario
    When i fill all field in User Story Scenario Form with title and apps desc
    And i press generate button in user scenario story
    Then i should see user story Scenario list
