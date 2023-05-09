from lib.multiclass_todolist import *

# #When I initialise the class, ensure a list is created.

# def test_initialise_empty_list_incomplete():
#     todo = TodoList()
#     assert todo.incomplete() == []

# def test_initialise_empty_list_complete():
#     todo = TodoList()
#     assert todo.complete() == []

# #When I initialise the class, ensure a task is being correctly added to the list.   

# def test_add_single_task_incomplete():
#     todo = TodoList()
#     task1 = "Walk the dog."
#     todo.add(task1)
#     assert todo.incomplete() == ["Walk the dog."]

# def test_add_single_task_complete():
#     todo = TodoList()
#     task1 = "Walk the dog."
#     todo.add(task1)
#     assert todo.complete() == ["Walk the dog."] 

# #When I initialise the class, ensure multiple tasks are being correctly added to the list.   

# def test_add_multiple_tasks_incomplete():
#     todo = TodoList()
#     task1 = "Walk the dog."
#     task2 = "Go to the shops."
#     todo.add(task1)
#     todo.add(task2)
#     assert todo.incomplete() == ["Walk the dog.", "Go to the shops."]

# def test_add_multiple_tasks_complete():
#     todo = TodoList()
#     task1 = "Walk the dog."
#     task2 = "Go to the shops."
#     todo.add(task1)
#     todo.add(task2)
#     assert todo.incomplete() == ["Walk the dog.", "Go to the shops."]      

