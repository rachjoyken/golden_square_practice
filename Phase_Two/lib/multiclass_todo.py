class Todo:

    def __init__(self, task):
        self.task = task
        self.completion_task = False   
        
    def mark_complete(self):
        self.completion_task = True
