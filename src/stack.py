class Stack():
    """stack"""
    def __init__(self):
        self._list = []
    
    def push(self, item):
        """..."""
        self._list.append(item)
        
    def pop(self):
        item = self._list.pop()
        return item  
    
    def peak(self):
        item = self._list[-1]
        return item
    
    def is_empty(self):
        if self._list == []:
            return True
        else:
            return False
    
    def size(self):
        return len(self._list)
    
if __name__ == "__main__":
    new_stack = Stack()
    for i in range(5):
        new_stack.push(i)
    print(new_stack.pop())
    print(new_stack.peak())
    print(new_stack.size())
    print(new_stack.is_empty())
    
