from lib.completed_tasks import *

def test_add_task():
    completed_task = CompletedTask()
    completed_task.add_task("Walk the dog")
    assert completed_task.list_tasks() == ["Walk the dog"]

def test_remove_task():
    completed_task = CompletedTask()
    completed_task.add_task("Walk the dog")
    completed_task.add_task("Go to the shop")
    completed_task.remove_task("Walk the dog")
    assert completed_task.list_tasks() == ["Go to the shop"] 