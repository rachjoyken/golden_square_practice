class TodoList:
    
    def __init__(self):
        self.incomplete_list = []
        self.complete_list = []

    def add(self, todo):
        self.incomplete_list.append(todo)
      
    def incomplete(self):
        return self.incomplete_list
    
    def complete(self):
        for x in self.incomplete_list:
            if x.completion_task == True:
                self.complete_list.append(x)
                self.incomplete_list.remove(x)
        return self.complete_list          

    def give_up(self):
        for x in self.incomplete_list:
            x.completion_task == True
            self.complete_list.append(x) 
            self.incomplete_list.clear()
            return self.complete_list
    


    

    
    