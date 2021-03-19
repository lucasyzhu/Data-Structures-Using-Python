class _Node():
    
    def __init__(self):
        self.value = None
        self.next = None

class LinkQueue():
    
    def __init__(self):
        head_node = _Node()
        self.front = head_node
        self.rear = head_node
    
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
    
    def enter_queue(self, item):
        queue_node = _Node()
        queue_node.value = item
        self.rear.next = queue_node
        self.rear = queue_node
        print("An new item has been added: ", item)

    def delete_queue(self):
        if self.is_empty() == True:
            print("This queue is empty!")
            return False
        else:
            prev_node = self.front.next
            self.front.next = prev_node.next
            if self.rear == prev_node:
                self.rear = self.front
            return prev_node.value

    def get_head_queue(self):
        if self.is_empty() == True:
            print("No head item")
        else:
            return self.front.next.value

if __name__=='__main__':
     new_queue = LinkQueue()
     print(new_queue.is_empty())
     print(new_queue.get_head_queue())
     for i in range(10):
        new_queue.enter_queue(i)

     print(new_queue.delete_queue())
     print(new_queue.get_head_queue())

