

## 1. Describe the Problem

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class CompletedTasks()

    def __init__(self):
        #assign a variable to an empty list for storage of tasks

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass 

     def delete_task(self, task):
        #Parameters:
        # task: string representing a single task to be deleted
        # Returns:
        # Nothing
        # Side-effects
        # Removes the task 
        pass

    def list_tasks(self):
        # Returns:
        #   A list of all tasks - added, completed(deleted)
        # Side-effects:
        #   Throws an exception if the list is empty
        pass 

   

```


## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
#adds task to list
"""
completed_tasks = CompletedTasks()
completed_tasks.add_task("Walk the dog")
completed_tasks.list_tasks() 

"""
Given no task
#add_task raises an exception if string is empty
"""
completed_tasks = CompletedTasks()
completed_tasks.add_task("") # raises an error with the message "No task set."

"""

"""
Given a task 
#delete_task deletes task

completed_tasks = CompletedTasks()
completed_tasks.delete_task("") # deletes the task from the list

"""

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._