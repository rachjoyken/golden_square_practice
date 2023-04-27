from lib.multiclass_diary import *
from lib.multiclass_diaryentry import *

def test_adds_and_lists_diary_entries():
        diary = Diary()
        entry1 = DiaryEntry("My Title1", "My Contents1")
        entry2 = DiaryEntry("My title2", "My Contents2")
        diary.add(entry1)
        diary.add(entry2)
        assert diary.all == [entry1, entry2]