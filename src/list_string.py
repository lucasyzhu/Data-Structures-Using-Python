class String():
    def __init__(self):
        self.max_size = 5
        self.chars = ""
        self.length = 0
    
    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False
    
    def create(self, new_string):
        if len(new_string) > self.max_size:
            print("Too long!")
            self.chars = new_string[:self.max_size]
        else:
            self.chars = new_string
        return self.chars

    



if __name__ == "__main__":
    string_src = String()
    print(string_src.is_empty())
    print(string_src.create("XiangJiangYang"))
