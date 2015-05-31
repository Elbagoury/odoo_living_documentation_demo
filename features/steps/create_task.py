__author__ = 'colinwren'

from datetime import datetime, timedelta

@given('I create a new task in a project')
def impl(ctx):
	# Get a project to add a task to
	projects = ctx.client.model('project.project').browse([])
	assert len(projects) > 0
	ctx.project_id = projects[0].id

	# create a new task object
	ctx.task_model = ctx.client.model('project.task')
	task = ctx.task_model.create({'name': 'Test Task', 'project_id': ctx.project_id})
	assert task

	ctx.task = task

@given('I assign it to no one')
def impl(ctx):
	pass

@given('I assign it to {user_name}')
def impl(ctx, user_name):
	# find a user with that user name
	ctx.user_model = ctx.client.model('res.users')
	ctx.user_id = ctx.user_model.search([['name', '=', user_name]])
	assert len(ctx.user_id) > 0

	# assign the task to the user
	ctx.task.write({'user_id': ctx.user_id[0]})

@given('I set {product_manager_name} to review the developer\'s work')
def impl(ctx, product_manager_name):
	# find a user with that user name
	ctx.user_model = ctx.client.model('res.users')
	ctx.reviewer_id = ctx.user_model.search([['name', '=', product_manager_name]])
	assert len(ctx.reviewer_id) > 0

	# assign the task to the user
	ctx.task.write({'reviewer_id': ctx.reviewer_id[0]})

@given('set it to be due in a weeks time')
def impl(ctx):
	now_date = datetime.now()
	then_date = now_date + timedelta(days=7)
	ctx.test_date = datetime.strftime(then_date, '%Y-%m-%d')
	ctx.task.write({'date_deadline': ctx.test_date})

@given('I want to group the task with similar tasks via a "BDD" tag')
def impl(ctx):
	# create a tag
	proj_cat = ctx.client.model('project.category')
	ctx.tag = proj_cat.create({'name': 'BDD'})
	ctx.task.write({'categ_ids': [ctx.tag.id]})

@given('I add a description to help the developer understand the task')
def impl(ctx):
	ctx.task.write({'description': 'This is a description'})

@given('I set the stage to "Development" as it needs attention straight away')
def impl(ctx):
	# get the stage for Development
	stage_model = ctx.client.model('project.task.type')
	stages = stage_model.search([['name', '=', 'Development']])
	assert len(stages) > 0
	ctx.stage = stages[0]

	# set the stage to development
	ctx.task.write({'stage_id': ctx.stage})


@when('I view the project\'s task list for {user_name}')
def impl(ctx, user_name):
	# search project.task for tasks for user
	user_id = ctx.user_model.search([['name', '=', user_name]])
	tasks = ctx.task_model.search([['user_id', '=', user_id]])
	assert len(tasks) > 0

	ctx.task_list = tasks

@when('I search the project\'s task list for tasks to be reviewed by {product_manager_name}')
def impl(ctx, product_manager_name):
	# search project.task for tasks for user
	user_id = ctx.user_model.search([['name', '=', product_manager_name]])
	tasks = ctx.task_model.search([['reviewer_id', '=', user_id]])
	assert len(tasks) > 0

	ctx.task_list = tasks

@when('I search the project\'s task list for tasks with the "BDD" tag')
def impl(ctx):
	tasks = ctx.task_model.search([['categ_ids', 'in', ctx.tag.id]])
	assert len(tasks) > 0
	ctx.task_list = tasks

@when('I view the project\'s task list')
def impl(ctx):
	# search project.task for tasks for user
	tasks = ctx.task_model.search([['project_id', '=', ctx.project_id]])
	assert len(tasks) > 0

	ctx.task_list = tasks

@when('I view the task')
def impl(ctx):
	task_obj = ctx.task_model.read(ctx.task.id)
	assert task_obj
	ctx.task_obj = task_obj

@when('I search the project\'s task list for tasks in "Development"')
def impl(ctx):
	tasks = ctx.task_model.search([['stage_id', '=', ctx.stage]])
	assert len(tasks) > 0
	ctx.task_list = tasks

@then('I can see the task in the list')
def impl(ctx):
	# check that the task ID is in the list
	assert ctx.task.id in ctx.task_list

@then('I can see the task I assigned to {developer_name}')
def impl(ctx, developer_name):
	assert ctx.task.id in ctx.task_list

@then('I can see the deadline for task')
def impl(ctx):
	tasks = ctx.task_model.read([ctx.task.id])
	assert len(tasks) > 0
	task = tasks[0]
	assert task['date_deadline'] == ctx.test_date

@then('I can see the tasks associated with the "BDD" tag')
def impl(ctx):
	assert ctx.task.id in ctx.task_list

@then('I can see the description')
def impl(ctx):
	assert ctx.task_obj['description'] == 'This is a description'