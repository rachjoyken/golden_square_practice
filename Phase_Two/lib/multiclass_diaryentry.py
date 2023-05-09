from math import ceil

class DiaryEntry:

    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        self.stop_off_point = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        word_count = self.count_words()
        return ceil(word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        readable_chunk_length = wpm * minutes
        words = self.contents.split()
        start_point = self.stop_off_point
        end_point = self.stop_off_point + readable_chunk_length
        readable_chunk = " ".join(words[start_point:end_point])
        self.stop_off_point += readable_chunk_length
        return readable_chunk