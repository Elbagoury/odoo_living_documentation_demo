@task_management_create_task
Feature: Create a Task
  In order to turn the product managers specification into a product
  As a development team lead
  I want to create tasks for the developers so they can build the components needed

  @create_task_user
  Scenario Outline: Create a task for a particular user
    Given I want to create a task for <developer_name>
    When I create a new task
    Then I should be able to assign the task to <developer_name>

    Examples:
    | developer_name |
    | Colin          |
    | Joel           |
    | Will           |
    | Lorenzo        |

  Scenario: Create a task with no user so it can be pulled by a developer at a later date
    Given I want to create a task with no user
    When I create a new task
    Then I should be able to create the task without assigning it to a user

  @create_task_user
  Scenario Outline: Create a task and assign a person to review the task
    Given I want to create a task for <developer_name>
    And I want <product_manager_name> to review the developer's work
    When I create a new task
    Then I should be able to assign the task to <developer_name>
    And I should be able to set <product_manager_name> as the task's reviewer

    Examples:
    | developer_name | product_manager_name |
    | Colin          | Eckhard              |
    | Joel           | Julian               |
    | Will           | Eckhard              |
    | Lorenzo        | Rob                  |


  @create_task_deadline
  Scenario: Create a task with a deadline
    Given I want to create a task that is due on a particular date
    When I create a new task
    Then I should be able to assign a deadline to the task

  Scenario: Create a task with a tag
    Given I want to create a task
    And I want to group the task with similar tasks
    When I create a new task
    Then I should be able to assign a tag

  Scenario: Create a task with a description
    Given I want to create a task that has a lot of background to it
    When I create a new task
    Then I should be able to add as much text as needed into the description field

  @create_task_deadline
  Scenario: Create a task with an initial stage
    Given I want to create a task that needs attention straight away
    When I create a new task
    Then I should be able to set it's stage to "Development" when I create it

  @create_task_deadline
  Scenario: Create a task with a priority
    Given I want to create a task that needs attention straight away
    When I create a new task
    Then I should be able to set it's priority to "High"
