class Diary_Entry:

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def word_count(self):
        return len(self.contents.split())