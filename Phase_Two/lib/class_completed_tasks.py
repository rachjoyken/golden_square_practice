class CompletedTask():
    def __init__(self):
        self.list = []

    def add_task(self, task):
        if task == "":
            raise Exception("Please enter a task.")
        self.list.append(task)
        
    def list_tasks(self):
        return self.list
    
    def remove_task(self, task):
        self.list.remove(task)