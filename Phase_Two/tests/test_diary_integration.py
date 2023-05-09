from lib.multiclass_diary import *
from lib.multiclass_diaryentry import *

def test_adds_and_lists_diary_entries():
        diary = Diary()
        entry1 = DiaryEntry("My Title1", "My Contents1")
        entry2 = DiaryEntry("My title2", "My Contents2")
        diary.add(entry1)
        diary.add(entry2)
        assert diary.all() == [entry1, entry2]

def test_count_words_returns_count_all_words_in_all_entry_contents():
        diary = Diary()
        entry1 = DiaryEntry("My Title1", "One, Two")
        entry2 = DiaryEntry("My title2", "Three, Four")
        diary.add(entry1)
        diary.add(entry2)
        assert diary.count_words() == 4

#Given I add two diary entries with a total length of 5 and I call #reading_time with a wpm of 2, then the total reading time should be 3(rounded up from 2.5)

def test_reading_time_returns_time_to_read_all_entries():
        diary = Diary()
        entry1 = DiaryEntry("My Title1", "One Two")
        entry2 = DiaryEntry("My title2", "Three Four Five")
        diary.add(entry1)
        diary.add(entry2)
        assert diary.reading_time(2) == 3

#Given I add two diary entries, one long and one short. #And I call #find_best_entry_for_reading_time.        
#With a wpm and minutes that means I can only read the short one. 
#Then #find_best_entry_for_reading_time returns the shorter entry 
#(e.g. below - wpm of 2 with 3 mins to read, means the reader can read 6 words in 3 mins, so cannot read entry2 as it's too long)

def test_find_best_entry_for_reading_time_returns_entry_that_fits_in_time():
        diary = Diary()
        entry1 = DiaryEntry("My Title1", "One two three")
        entry2 = DiaryEntry("My title2", "One two three four five six seven")
        diary.add(entry1)
        diary.add(entry2)
        assert diary.find_best_entry_for_reading_time(2, 3) == entry1

#Gven I add a diary entry      
#And I call #find_best_entry_for_reading_time
#With a wpm and minutes that means I can read that entry
#Then #find_best_entry_for_reading_time returns that entry

def test_find_best_entry_for_reading_time_returns_single_entry_that_fits_in_time():
    diary = Diary()
    entry1 = DiaryEntry("My Title1", "One two three")
    diary.add(entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1

#Given I add a diary entry
#And I call #find_best_entry_for_reading_time
#With a wpm and minutes that means I cannot read that entry
#Then find_best_entry_for_reading_time returns None

def test_find_best_entry_for_reading_time_returns_none_if_single_entry_doesnt_fit():
    diary = Diary()
    entry1 = DiaryEntry("My Title1", "One two three four five six seven")
    diary.add(entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

#Given I add two diary entries    
#And I call #find_best_entry_for_reading_time
#With a wpm and minutes that means I could read both
#Then #find_best_entry_for_reading_time returns the longer one

def test_find_best_entry_for_reading_time_returns_the_longer_entry():
        diary = Diary()
        entry1 = DiaryEntry("My Title1", "One two three")
        entry2 = DiaryEntry("My title2", "One two three four five six seven")
        diary.add(entry1)
        diary.add(entry2)
        assert diary.find_best_entry_for_reading_time(2, 4) == entry2
