class Deque():
    
    def __init__(self):
        self._list = []
     
    def is_empty(self):
        if self._list == []:
            return True
        else:
            return False
        
    def add_front(self, item):
        self._list.insert(0, item)
        return True
    
    def add_rear(self, item):
        self._list.append(item)
        return True
    
    def remove_front(self):
        item = self._list.pop(0)
        return item
    
    def remove_rear(self):
        item = self._list.pop()
        return item
    
    def size(self):
        return len(self._list)
    
    
if __name__ == "__main__":
    new_queue = Deque()
    
    for i in range(5):
        new_queue.add_rear(i)
    
    print(new_queue.remove_rear())
    print(new_queue.size())
    print(new_queue.is_empty())   