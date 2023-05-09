from lib.multiclass_todo import *
from lib.multiclass_todolist import *

# # def test_add_single_task():
# #     todo = TodoList()
# #     task1 = Todo("Walk the dog.")
# #     task2 = Todo("Go to the shop.")
# #     task3 = Todo("Hoover.")
# #     todo.add(task1)
# #     todo.add(task2)
# #     todo.add(task3)
# #     todo.incomplete
# #     task1.mark_complete      
# #     todo.incomplete 
# #     todo.give_up 

#When I initialise with a task,
#This single task is added to our incomplete list.

def test_add_single_task_to_incomplete_list():
    todo = TodoList()
    task1 = Todo("Walk the dog.")
    todo.add(task1)
    assert todo.incomplete() == [task1]

#When I initialise with a task,
#This single task is not added to our complete list.

def test_single_task_not_added_to_complete_list():
    todo = TodoList()
    task1 = Todo("Walk the dog.")
    todo.add(task1)
    assert todo.complete() == []

#When I mark a single task as complete, it's added to the complete list and removed from the incomplete list.

def test_mark_single_task_as_complete():
    todo = TodoList()
    task1 = Todo("Walk the dog.")
    task1.mark_complete()
    todo.add(task1)
    assert todo.complete() == [task1]
    assert todo.incomplete() == []

#When I add two tasks to our todo list and mark one as complete, the completed task will appear in the completed list and the other task will remain in the incomplete list.

def test_add_two_tasks_complete_one():
    todo = TodoList()
    task1 = Todo("Walk the dog.")
    task2 = Todo("Go to the shop.")
    todo.add(task1)
    todo.add(task2)
    task1.mark_complete()
    assert todo.complete() == [task1]
    assert todo.incomplete() == [task2]

#When I add two tasks and 'give up', these tasks are all marked as complete (removed from the incomplete list and added to the complete list).

def test_add_two_tasks_and_give_up():
    todo = TodoList()
    task1 = Todo("Walk the dog.")
    task2 = Todo("Go to the shop.")
    todo.add(task1)
    todo.add(task2)
    assert todo.give_up() == [task1, task2]

def test_add_three_tasks_and_give_up():
    todo = TodoList()
    task1 = Todo("Walk the dog.")
    task2 = Todo("Go to the shop.")
    task3 = Todo("Hoover the living room.")
    todo.add(task1)
    todo.add(task2)
    todo.add(task3)
    assert todo.give_up() == [task1, task2, task3]    

        




    