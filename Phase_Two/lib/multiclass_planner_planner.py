from math import ceil
import re

class Planner:

    def __init__(self):
        self.diary_list = []
        self.todo_list = []
        self.contact_list = []

    def add_to_diary_list(self, entry):
        self.diary_list.append(entry)

        string = entry.contents
        result = re.findall(r'07\d{9}|\+447\d{9}', string)

        self.contact_list.append(result)

        # for entry in self.diary_list:
        #         if result in entry.contents:
        #             self.contact_list.append(entry)
         
    def add_to_todo_list(self, task):
        self.todo_list.append(task)

    def read_all(self):
        return self.diary_list 
    
    def read_contacts(self):
        return self.contact_list
        # contact_list = self.contact_list
        # for x in contact_list:
        #     return x.contents

    def word_count(self):
        word_count = [entry.word_count() for entry in self.diary_list]
        return sum(word_count)

    def reading_time(self, wpm):
       word_count = self.word_count()
       return ceil(word_count / wpm)
    
    def best_entry_for_reading_time(self, wpm, minutes):
        words_the_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0

        for entry in self.diary_list:
            if entry.word_count() <= words_the_user_could_read:
                if entry.word_count() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.word_count()
        return most_readable            