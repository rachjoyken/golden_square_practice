from lib.multiclass_planner_todo import *

"""
When I initialise the method with a task
The task is returned

"""
def test_initialise_with_single_task():
    todo = Todo("Walk the dog")
    assert todo.task == "Walk the dog"