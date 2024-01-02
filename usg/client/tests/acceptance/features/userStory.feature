@order3
Feature: User Story
    Scenario: Input Apps Desc
    Given i am on Dashboard Page
    When i press add project button
    Then i should be on input user story page
    When i fill all field in User Story Form with title and apps desc
    And i press generate button
    Then i should see user story list