from lib.multiclass_planner_diary_entry import *

"""
When I initialise the method with a title and contents
They are returned
"""
def test_initialise_title_and_contents_are_returned():
    diary_entry = Diary_Entry("Title", "Some contents")
    assert diary_entry.title == "Title"
    assert diary_entry.contents == "Some contents" 