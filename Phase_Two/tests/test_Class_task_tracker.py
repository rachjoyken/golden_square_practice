import pytest
from lib.Class_task_tracker import *

# def test_add_single_task():
#     task_tracker = TaskTracker()
#     assert task_tracker.add_task("Go to the shop.") == ["Go to the shop."]
#     # assert task_tracker.list_tasks()

# def test_add_multiple_tasks():
#     task_tracker = TaskTracker()
#     task_tracker.add_task("Walk the dog.")
#     assert task_tracker.add_task("Go to the shop.") == ["Walk the dog.", "Go to the shop."]

def test_list_tasks():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog.")
    assert task_tracker.list_tasks() == ["Walk the dog."]

def test_blank_string():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e:
        task_tracker.add_task("")
    error_message = str(e.value)
    assert error_message == "Please enter a task."