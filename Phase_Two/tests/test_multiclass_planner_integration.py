from lib.multiclass_planner_planner import *
from lib.multiclass_planner_diary_entry import *
from lib.multiclass_planner_todo import *

"""
Given a single diary entry of title and contents
I want to add this to the diary_list
"""
def test_add_single_dary_entry_to_diary_list():
    planner = Planner()
    diary_entry1 = Diary_Entry("Title", "Some contents")
    planner.add_to_diary_list(diary_entry1)
    assert planner.diary_list == [diary_entry1]


"""
Given multiple diary entries 
I want to add all entries to the diary_list
"""
def test_add_multiple_diary_entries_to_diary_list():
    planner = Planner()
    diary_entry1 = Diary_Entry("Title", "Some contents")
    diary_entry2 = Diary_Entry("Title2", "Some more contents")
    planner.add_to_diary_list(diary_entry1)
    planner.add_to_diary_list(diary_entry2)
    assert planner.diary_list == [diary_entry1, diary_entry2]


"""
When I add a single diary entry to the list
and call upon the read_all method it returns the single diary entry
"""
def test_add_single_diary_entry_return_this_in_read_all_list():
    planner = Planner()
    diary_entry1 = Diary_Entry("Title", "Some contents")
    planner.add_to_diary_list(diary_entry1)
    assert planner.read_all() == [diary_entry1]

"""
Given a single Todo Task
I want to add this to the todo_list
"""
def test_add_single_task_to_todo_list():
    planner = Planner()
    task1 = Todo("Walk the dog")
    planner.add_to_todo_list(task1)
    assert planner.todo_list == [task1]

"""
Given multiple Todo Tasks
I want to add all tasks to the todo_list
"""
def test_add_multiple_tasks_to_todo_list():
    planner = Planner()
    task1 = Todo("Walk the dog")
    task2 = Todo("go to the shops")
    task3 = Todo("hoover")
    planner.add_to_todo_list(task1)
    planner.add_to_todo_list(task2)
    planner.add_to_todo_list(task3)
    assert planner.todo_list == [task1, task2, task3]

"""
word_count
If I add a single entry with Title and contents with 5 words
this returns 5
"""
def test_singe_entry_contents_of_five_words_returns_word_count_five():
    planner = Planner()
    diary_entry1 = Diary_Entry("Title", "Some contents that add up")
    planner.add_to_diary_list(diary_entry1)
    assert planner.word_count() == 5

"""
word_count
If I add multiple entries with total contents of 10 words
this returns 10
"""
def test_multiple_entry_contents_of_ten_words_returns_word_count_ten():
    planner = Planner()
    diary_entry1 = Diary_Entry("Title", "Some contents that add up")
    diary_entry2 = Diary_Entry("Title", "one two three four five")
    planner.add_to_diary_list(diary_entry1)
    planner.add_to_diary_list(diary_entry2)
    assert planner.word_count() == 10

"""
When I initialise with a five-word content
then #reading_time with a wpm of 2, should return 3
"""
def test_single_entry_five_word_content_wpm2_returns_3():
    planner = Planner()
    diary_entry1 = Diary_Entry("My Title", "one two three four five")
    planner.add_to_diary_list(diary_entry1)
    assert planner.reading_time(2) == 3


"""
Given I add two diary entries with a total length of 7
and I call #reading_time with a wpm of 2,
then the total reading time should be 4(rounded up from 3.5)
"""
def test_multiple_entries_seven_word_content_wpm2_returns_4():
        planner = Planner()
        diary_entry1 = Diary_Entry("My Title1", "One Two")
        diary_entry2 = Diary_Entry("My title2", "Three Four Five Six Seven")
        planner.add_to_diary_list(diary_entry1)
        planner.add_to_diary_list(diary_entry2)
        assert planner.reading_time(2) == 4

"""
Given I add a diary entry
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can read that entry
Then #find_best_entry_for_reading_time returns that entry
"""
def test_find_best_entry_for_reading_time_returns_single_entry_that_fits_in_time():
        planner =Planner()
        diary_entry1 = Diary_Entry("My title2", "One two three")
        planner.add_to_diary_list(diary_entry1)
        assert planner.best_entry_for_reading_time(2, 3) == diary_entry1


"""
Given I add two diary entries, one long and one short. And I call find_best_entry_for_reading_time.
With a wpm and minutes that means I can only read the short one.
Then #find_best_entry_for_reading_time returns the shorter entry
(e.g. below - wpm of 2 with 3 mins to read, means the reader can read 6 words in 3 mins, so cannot read entry2 as it's too long)
"""

def test_find_best_entry_for_reading_time_returns_the_only_entry_that_fits_in_time():
        planner =Planner()
        diary_entry1 = Diary_Entry("My Title1", "One two three")
        diary_entry2 = Diary_Entry("My title2", "One two three four five six seven")
        planner.add_to_diary_list(diary_entry1)
        planner.add_to_diary_list(diary_entry2)
        assert planner.best_entry_for_reading_time(2, 3) == diary_entry1

"""
Given I add two diary entries.
And I call #find_best_entry_for_reading_time.
With a wpm and minutes that means I can read both.
Then #find_best_entry_for_reading_time returns the longer entry.
"""   

def test_find_best_entry_for_reading_time_returns_longer_entry_of_2_that_fit():
        planner =Planner()
        diary_entry1 = Diary_Entry("My Title1", "One two three")
        diary_entry2 = Diary_Entry("My title2", "One two three four five")
        planner.add_to_diary_list(diary_entry1)
        planner.add_to_diary_list(diary_entry2)
        assert planner.best_entry_for_reading_time(2, 3) == diary_entry2

"""
Given I add a single diary entry that only contains a mobile phone number.
The mobile number is detected and added to our contact list.
When I call #read_contacts, the mobile number is returned to us in a list.
"""        

def test_single_diary_entry_with_one_mobile_number():
    planner = Planner()
    diary_entry1 = Diary_Entry("title", "07780662996")
    planner.add_to_diary_list(diary_entry1)
    assert planner.read_contacts() == [["07780662996"]]

"""
Given I add multiple diary entries that each contain a mobile phone number.
The mobile numbers are detected and added to our contact list.
When I call #read_contacts, the mobile numbers are returned to us in a list.
"""        

def test_multiple_diary_entry_with_one_mobile_number():
    planner = Planner()
    diary_entry1 = Diary_Entry("title", "07780662996")
    planner.add_to_diary_list(diary_entry1)
    assert planner.read_contacts() == [["07780662996"]]    

 

