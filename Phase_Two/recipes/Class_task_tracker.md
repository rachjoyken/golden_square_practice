

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker:

    def __init__(self):
        pass 

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass 

    def list_tasks(self):
        # Returns:
        #   A list of all tasks
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
tracker = TaskTracker()
tracker.add_task("Walk the dog")
tracker.list_tasks() # => ["Walk the dog, Kay!"]

"""
Given no task
#add_task raises an exception if string is empty
"""
tracker = TaskTracker()
tracker.add_task("") # raises an error with the message "No task set."

"""

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
