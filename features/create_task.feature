@task_management_create_task
Feature: Create a Task
  In order to turn the product managers specification into a product
  As a development team lead
  I want to create tasks for the developers so they can build the components needed

  @create_task_user
  Scenario Outline: Create a task for a particular user
    Given I create a new task in a project
    And I assign it to <developer_name>
    When I view the project's task list for <developer_name>
    Then I can see the task in the list

    Examples:
    | developer_name |
    | Colin          |
    | Joel           |
    | Will           |
    | Lorenzo        |

  Scenario: Create a task with no user so it can be pulled by a developer at a later date
    Given I create a new task in a project
    And I assign it to no one
    When I view the project's task list
    Then I can see the task in the list

  @create_task_user
  Scenario Outline: Create a task and assign a person to review the task
    Given I create a new task in a project
    And I assign it to <developer_name>
    And I set <product_manager_name> to review the developer's work
    When I search the project's task list for tasks to be reviewed by <product_manager_name>
    Then I can see the task I assigned to <developer_name>

    Examples:
    | developer_name | product_manager_name |
    | Colin          | Eckhard              |
    | Joel           | Julian               |
    | Will           | Eckhard              |
    | Lorenzo        | Rob                  |


  @create_task_deadline
  Scenario: Create a task with a deadline
    Given I create a new task in a project
    And set it to be due in a weeks time
    When I view the project's task list
    Then I can see the deadline for task

  Scenario: Create a task with a tag
    Given I create a new task in a project
    And I want to group the task with similar tasks via a "BDD" tag
    When I search the project's task list for tasks with the "BDD" tag
    Then I can see the tasks associated with the "BDD" tag

  Scenario: Create a task with a description
    Given I create a new task in a project
    And I add a description to help the developer understand the task
    When I view the task
    Then I can see the description

  @create_task_deadline
  Scenario: Create a task with an initial stage
    Given I create a new task in a project
    And I set the stage to "Development" as it needs attention straight away
    When I search the project's task list for tasks in "Development"
    Then I can see the task in the list

  @create_task_deadline
  Scenario: Create a task with a priority
    Given I create a new task in a project
    And I set a "High" priority as it needs attention straight away
    When I view the project's task list
    Then I can see the task has a "High" priority
