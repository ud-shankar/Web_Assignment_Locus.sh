Feature: SDET Web assignment for Locus.sh
  Testing multiple scenarios as mentioned in the excel sheet.

  Scenario: Login with invalid credentials
    Given User navigates to Locus hiring dashboard
    When User is login page
    And User enter invalid user id and click continue
    Then User enters invalid password and try to login
    Then Alert message is displayed for invalid password

  Scenario: Login with valid credentials
    Given User navigates to Locus hiring dashboard
    When User is login page
    And User enter valid user id and click continue
    Then User enters valid password and try to login
    Then User is in Home page

  Scenario: User verified/Check personnel profile
    Given User navigates to Locus hiring dashboard
    When User is login page
    And User enter valid user id and click continue
    Then User enters valid password and try to login
    Then User is in Home page
    Then User hovers over profile icon and verify personal details

  Scenario: User searches for a task with task id
    Given User navigates to Locus hiring dashboard
    When User is login page
    And User enter valid user id and click continue
    Then User enters valid password and try to login
    Then User is in Home page
    Then User searches for a existing task and verify the search result

  Scenario: User creates a new task and searches for the created task
    Given User navigates to Locus hiring dashboard
    When User is login page
    And User enter valid user id and click continue
    Then User enters valid password and try to login
    And User is in Home page
    And User clicks on add task button and enter id, team
    Then User enters address, slot and change visit type to Service
    Then User clicks on create task and verifies ticket is created
    Then User searches for a created task and verify the search result
