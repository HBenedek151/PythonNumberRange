Feature: Is it in range?

Scenario Outline: Is it or is it not in range
    Given The number is <number>
    When The number is in range
    Then I should be told "<answer>"


Examples:
    |number | answer    |
    |7      | True      |
    |110    | False     |
    |-4     | False     |
    |0      | True      |
    |100    | True      |
    |6.7    | True      |
    |-1.3   | False     |