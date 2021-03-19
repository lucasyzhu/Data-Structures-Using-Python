class LoopQueue():
    
    def __init__(self, maximum):
        self.queue = [None] * maximum
        self.maximum = maximum
        self.front = 0
        self.rear = 0
    
    def enqueue(self, item):
        if (self.rear + 1) % self.maximum == self.front:
            print("ERROR: FULL!")
            return False
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.maximum
            return True
    
    def dequeue(self):
        if self.front == self.rear:
            print("ERROR: EMPTY!")
            return False
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maximum
            print(True)
            return item
    
    def print_data(self):
        cur = self.front
        while cur != self.rear:
            print(self.queue[cur])
            cur = (cur + 1) % self.maximum
            
    def length(self):
        size = (self.rear - self.front + self.maximum) % self.maximum
        return size
            
        
if __name__ == "__main__":
    new_queue = LoopQueue(5)
    print(new_queue.enqueue(3))
    print(new_queue.enqueue(4))
    print(new_queue.enqueue(5))
    
    print(new_queue.dequeue())
    new_queue.print_data()
    print(new_queue.length())