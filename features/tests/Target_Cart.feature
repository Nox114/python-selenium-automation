
Feature: Tests Cart


  Scenario: User can open cart and see "Your cart is empty" message
    Given Open target main page
    When Click on cart icon
    Then Verify "Your cart is empty" message shown