from lib.multiclass_planner_planner import *

"""
When I initialise the class
three empty lists are created
"""
def test_initialise_three_empty_lists_created():
    planner = Planner()
    assert planner.diary_list == []
    assert planner.todo_list == []
    assert planner.contact_list == []


"""
When I initialise the PLanner class
and call the read_all method without adding any entries
an empty list is returned
"""
def test_no_entries_read_all_empty_list():
    planner = Planner()
    planner.read_all()
    assert planner.diary_list == []


"""
If the are no entries in the diary_list
this returns 0 words for word.count
"""
def test_no_entries_word_count_zero():
    planner = Planner()
    planner.word_count()
    assert planner.word_count() == 0
  