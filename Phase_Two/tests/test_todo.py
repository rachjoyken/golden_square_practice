from lib.multiclass_todo import *

#Given a single task, check that the task's 'completion property' is set to False by default.

def test_single_task_set_to_False():
    task1 = Todo("Walk the dog.")
    assert task1.completion_task == False

#Given a single task is marked as complete, check that the task's 'completion property' switches to True.

def test_single_task_changes_to_True():
    task1 = Todo("Walk the dog.")
    task1.mark_complete()
    assert task1.completion_task == True
