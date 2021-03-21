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
    
    def enqueue(self, item):
        queue_node = _Node()
        queue_node.value = item
        self.rear.next = queue_node
        self.rear = queue_node
        print("An new item has been added: ", item)

    def dequeue(self):
        if self.is_empty() == True:
            print("This queue is empty!")
            return False
        else:
            prev_node = self.front.next
            self.front.next = prev_node.next
            if self.rear == prev_node:
                self.rear = self.front
            return prev_node.value

    def get_head(self):
        if self.is_empty() == True:
            print("No head item")
        else:
            return self.front.next.value
    
    def traverse(self):
        if self.is_empty() == True:
            return "It is empty queue!"
        else:
            queue_node = self.front.next
            queue_list = []
            while queue_node != None:
                queue_list.append(queue_node.value)
                queue_node = queue_node.next
            return queue_list
    
    def size(self):
        if self.is_empty() == True:
            return 0
        else:
            queue_node = self.front.next
            count = 0 
            while queue_node != None:
                queue_node = queue_node.next
                count += 1
            return count


if __name__ == '__main__':
     new_queue = LinkQueue()
     print(new_queue.is_empty())
     print(new_queue.get_head())
     for i in range(10):
        new_queue.enqueue(i)

     print(new_queue.dequeue())
     print(new_queue.get_head())
     print(new_queue.traverse())
     print(new_queue.size())