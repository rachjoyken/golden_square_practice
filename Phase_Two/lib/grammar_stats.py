class GrammarStats:
    def __init__(self):
        self.checks_done = 0
        self.checks_passed = 0
  
    def check(self, text):
        self.text = text
        special_characters = ".!?"
        self.checks_done +=1
        if text[0].isupper() and text[-1] in special_characters:
            self.checks_passed +=1
            return True
        else:
            return False

  
    def percentage_good(self):
        result = self.checks_passed / self.checks_done * 100
        print(result)
        return int(result)