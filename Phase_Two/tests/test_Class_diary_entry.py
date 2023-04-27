from lib.class_diary_entry import *

def test_title_and_content_as_string():
    diary_entry = DiaryEntry("Day 1", "contents")
    assert diary_entry.format() == "Day 1: contents"
def test_count_words():
    diary_entry = DiaryEntry("Day 1", "contents")
    assert diary_entry.count_words() == 3
def test_wpm():
    diary_entry = DiaryEntry("Day 1", "contents")
    assert diary_entry.reading_time(3) == 1
def test_reading_chunk():
    diary_entry = DiaryEntry("Day 1", "contents1 contents2 contents3 contents4 contents5 contents6 contents7 contents8")
    assert diary_entry.reading_chunk(1, 2) == "contents1 contents2"
    assert diary_entry.reading_chunk(3, 2) == "contents3 contents4 contents5 contents6 contents7 contents8"
    assert diary_entry.reading_chunk(2, 1) == "contents1 contents2"