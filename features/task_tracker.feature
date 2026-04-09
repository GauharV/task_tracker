Feature: Task Tracker

  Background:
    Given the user navigates to "http://localhost:5000"

  Scenario: Successfully adding a task
    Given the user is on the task list page
    When the user adds a task "Buy milk"
    Then the task list should contain "Buy milk"

  Scenario: Submitting an empty task shows an error
    Given the user is on the task list page
    When the user submits an empty task
    Then an error message "Task cannot be empty" should be displayed
