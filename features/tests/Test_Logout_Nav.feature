
Feature: Tests Sign in


  Scenario: User can navigate to sign while logged out
    Given Open target main page
    When Click on sign in
    Then Click on nav menu sign in
    Then Verify sign in form opened