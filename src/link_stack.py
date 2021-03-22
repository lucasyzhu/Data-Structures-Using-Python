class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkStack():
    def __init__(self):
        self._top = None
    
    def is_empty(self):
        if self._top == None:
            return True
        else:
            return False
    
    def push(self, item):
        node = Node(item)
        node.next = self._top
        self._top = node
        return True
    
    def pop(self):
        top_item = self._top
        self._top = self._top.next
        return top_item.value
    
    def top_item(self):
        return self._top.value
    
    def size(self):
        count = 0
        cur = self._top
        while(cur != None):
            count += 1
            cur = cur.next
        return count            
    
if __name__ == "__main__":
    new_stack = LinkStack()
    print(new_stack.is_empty())
        
    for i in range(5):
        print(new_stack.push(i))
   
    print(new_stack.top_item())
    print(new_stack.pop())
    print(new_stack.top_item())
    print(new_stack.is_empty())
    print(new_stack.size())    