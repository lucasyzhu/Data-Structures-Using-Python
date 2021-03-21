# 2021/03/21 v0.0.1

class _Node():
    def __init__(self):
        self.value = None
        self.next = None


class CircularLinkQueue():
    def __init__(self):
        self.rear = _Node()
        self.rear.next = self.rear
        self.length = 0

    def is_empty(self):
        if self.rear.next == self.rear:
            return True
        else:
            return False
    
    def enqueue(self, item):
        queue_node = _Node()
        queue_node.value = item
        queue_node.next = self.rear.next
        self.rear.next = queue_node
        self.rear = self.rear.next
        self.length += 1
        print("An new item has been added: ", item)


    def dequeue(self):
        if self.is_empty() == True:
            print("This queue is empty!")
            return False
        else:
            queue_node = self.rear.next.next
            self.rear.next.next = queue_node.next
            queue_node.next == None
            if queue_node == self.rear:
                self.rear = self.rear.next
            self.length -= 1
            return queue_node.value

    def traverse(self):
        if self.is_empty() == True:
            return "No head item"
        else:
            queue_node = self.rear.next.next
            queue_list = []
            while queue_node != self.rear.next:
                queue_list.append(queue_node.value)
                queue_node = queue_node.next
            return queue_list


    def get_head(self):
        if self.is_empty() == True:
            return "No head item!"
        else:
            return self.rear.next.next.value

    def size(self):
        return self.length

if __name__ == "__main__":
    new_queue = CircularLinkQueue()
    print(new_queue.is_empty())
    print(new_queue.size())
    print(new_queue.get_head())
    for i in range(10):
        new_queue.enqueue(i)
    print(new_queue.get_head())
    print(new_queue.dequeue())
    print(new_queue.traverse())
    print(new_queue.size())
    