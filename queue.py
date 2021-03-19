class Queue():
    
    def __init__(self):
         self._list = []
         
    def enqueue(self, item):
        self._list.append(item)
        return True
    
    def dequeue(self):
        item = self._list.pop(0)
        return item
    
    def is_empty(self):
        if self._list == []:
            return True
        else:
            return False
    
    def peak(self):
        return self._list[0]
    
    def size(self):
        return len(self._list)
    
if __name__ == "__main__":
    new_queue = Queue()
    
    for i in range(5):
        new_queue.enqueue(i)
    
    print(new_queue.dequeue())
    print(new_queue.peak())
    print(new_queue.size())
    print(new_queue.is_empty())