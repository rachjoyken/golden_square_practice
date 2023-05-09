1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

# 2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com



                             ┌─────────────────────────────┐
                             │ Planner Master              │
                             │                             │
                             │ __init__ Diary List, todo   │
                             │                             │
                             │ add_entry                   │
                             │ word_count                  │
                             │ Read_all                    │
                             │ reading_time 
                                best_entry_for_reading_time               │
                             │                             │
                ┌────────────┴──────────────┬──────────────┴────────────────┐
                │                           │                               │
                │                           │                               │
                │                           │                               │
                │                           │                               │
  ┌─────────────▼─────────────┐    ┌────────▼────────────┐   ┌──────────────▼──────┐
  │  Diary Entry              │    │   Todo              │   │   Mobile_Number     │
  │                           │    │                     │   │                     │
  │  __init__ Title,Contents  │    │   __init__ Task     │   │   __init__ Number   │
  │                           │    │                     │   │                     │
  │  word_count               │    │                     │   │                     │
  │  reading_time             │    └─────────────────────┘   └─────────────────────┘
  └───────────────────────────┘



Also design the interface of each class in more detail.


class Planner:
#   User-facing properties:
    # Diary List: list of diary entries
    # Todo List : list of tasks
    # Contact List : List of mobile phone numbers

    def __init__(self):
        pass # No code here yet
        # Side-effects:
        # Creats three empty lists

    def add_to_diary_list(self, entry):
        # Parameters:
        #   entry: an instance of Diary_Entry
        # Side-effects:
        # Adds the entry to the diary list
        # Checks string for phone numbers
        #Mobile Phone number regex (07\d{9}|+447\d{9})$
        pass # No code here yet

    def add_to_todo_list(self, task):
        # Parameters:
        #   task: an instance of Todo
        # Side-effects:
        #   Adds the Task to the Todo list
        pass # No code here yet

    def read_all(self):
        # Parameters:
        #   None
        # Side-effects:
        # Returns a list of all diary entries
        pass # No code here yet  

    def word_count(self):
        # Parameters:
        # None
        # Returns:
        # The length of a split string the number of words in the contents
        pass # No code here yet

    def reading_time(self, wpm):
        # Parameters:
        # wpm: number of words that can be read per minute
        # Returns:
        # The time it takes to read a particular entry based on a given wpm.
        pass # No code here yet

    def best_entry_for_reading_time(self, wpm, minutes)
        #Parameters:
        wpm : words per minute
        Minutes: Number of minutes available
        #Returns: 
        #The most appropriate contents of the diary that can be read within the time and wpm (returns the object instance)
        pass


class Diary_Entry
#   User-facing properties:
    # None

    def __init__(self, Title, Contents):
    pass # No code here yet
    # Side-effects:
    # sets the title and contents properties


Class Todo
#   User-facing properties:
    # None

    def __init__(self, task):
    pass # No code here yet
    # Side-effects:
    # sets the task properties



# 3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.


from math import ceil

# Integration

"""
Given a single diary entry of title and contents
I want to add this to the diary_list
"""
planner = PLanner()
diary_entry1 = Diary_Entry("Title", "Some contents")
planner.add_to_diary_list(diary_entry1)
assert self.diary_list #=> [diary_entry1]


"""
Given multiple diary entries 
I want to add all entries to the diary_list
"""
planner = PLanner()
diary_entry1 = Diary_Entry("Title", "Some contents")
diary_entry2 = Diary_Entry("Title2", "Some more contents")
planner.add_to_diary_list(diary_entry1)
planner.add_to_diary_list(diary_entry2)
assert self.diary_list #=> [diary_entry1, diary_entry2]


"""
When I add a single diary entry to the list
and call upon the read_all method it returns the single diary entry
"""
planner = PLanner()
diary_entry1 = Diary_Entry("Title", "Some contents")
planner.add_to_diary_list(diary_entry1)
assert planner.read_all() = [diary_entry1]

"""
Given a single Todo Task
I want to add this to the todo_list
"""
planner = PLanner()
task1 = Todo("Walk the dog")
planner.add_to_todo_list(task1)
assert self.todo_list #=> [task1]

"""
Given multiple Todo Tasks
I want to add all tasks to the todo_list
"""
planner = PLanner()
task1 = Todo("Walk the dog")
task2 = Todo("go to the shops")
task3 = Todo("hoover")
planner.add_to_todo_list(task1)
planner.add_to_todo_list(task2)
planner.add_to_todo_list(task3)
assert self.todo_list #=> [task1, task2, task3]

"""
word_count
If I add a single entry with Title and contents with 5 words
this returns 5
"""
planner = Planner()
diary_entry1 = Diary_Entry("Title", "Some contents that add up")
planner.add_to_diary_list(diary_entry1)
assert planner.word_count() #=> 5

"""
word_count
If I add multiple entries with total contents of 10 words
this returns 10
"""
planner = Planner()
diary_entry1 = Diary_Entry("Title", "Some contents that add up")
diary_entry2 = Diary_Entry("Title", "one two three four five")
planner.add_to_diary_list(diary_entry1)
planner.add_to_diary_list(diary_entry2)
assert planner.word_count() #=> 10

""
When I initialise with a five-word content
then #reading_time with a wpm of 2, should return 3
"""
def test_reading_time():
    planner = Planner()
    diary_entry1 = Diary_Entry("My Title", "one two three four five")
    planner.add_to_diary_list(diary_entry1)
    assert planner.reading_time(2) == 3


"""
Given I add two diary entries with a total length of 5
and I call #reading_time with a wpm of 2,
then the total reading time should be 3(rounded up from 2.5)
"""
def test_reading_time_returns_time_to_read_all_entries():
        diary = Diary()
        entry1 = DiaryEntry("My Title1", "One Two")
        entry2 = DiaryEntry("My title2", "Three Four Five")
        diary.add(entry1)
        diary.add(entry2)
        assert diary.reading_time(2) == 3

"""
Gven I add a diary entry
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can read that entry
Then #find_best_entry_for_reading_time returns that entry
"""
def test_find_best_entry_for_reading_time_returns_single_entry_that_fits_in_time():
        planner =Planner()
        diary_entry1 = Diary_Entry("My title2", "One two three")
        planner.add(diary_entry1)
        assert planner.best_entry_for_reading_time(2, 3) == diary_entry1

"""
Given I add two diary entries, one long and one short. #And I call #find_best_entry_for_reading_time.
With a wpm and minutes that means I can only read the short one.
Then #find_best_entry_for_reading_time returns the shorter entry
(e.g. below - wpm of 2 with 3 mins to read, means the reader can read 6 words in 3 mins, so cannot read entry2 as it's too long)
"""
def test_find_best_entry_for_reading_time_returns_entry_that_fits_in_time():
        planner =Planner()
        diary_entry1 = Diary_Entry("My Title1", "One two three")
        diary_entry2 = Diary_Entry("My title2", "One two three four five six seven")
        planner.add(diary_entry1)
        planner.add(diary_entry2)
        assert planner.best_entry_for_reading_time(2, 3) == diary_entry1



# 4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# Planner

"""
When I initialise the class
three empty lists are created
"""
planner = Planner()
assert Diary List # => []
assert Todo_list #=> []
assert Contact_List # => []


"""
When I initialise the PLanner class
and call the read_all method without adding any entries
an empty list is returned
"""
planner = Planner()
planner.read_all()
assert Diary List # => []


"""
If the are no entries in the diary_list
this returns 0 words
"""
planner = Planner()
planner.word_count()
assert planner.word_count() # => 


# Diary_Entry
"""
When I initialise the method with a title and contents
They are returned
"""
diary_entry = Diary_Entry("Title", "Some contents")
assert diary_entry.title #=> "Title"
assert diary_entry.content #=> "Some contents"


# Todo
"""
When I initialise the method with a taskt
The task is returned
"""
todo = Todo("Walk the dog")
assert todo.task #=> "Walk the dog"



# 5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

























