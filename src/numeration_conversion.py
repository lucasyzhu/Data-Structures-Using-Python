from stack import Stack

num = int(input('Pls input a decimal number: '))
sym = int(input('Pls input a systematic digit: '))
new_stack = Stack()

while(num != 0):
    new_stack.push(num % sym)
    num = num // sym

new_item = []
while(new_stack.is_empty() == 0):
    pop_item = new_stack.pop()
    new_item.append(pop_item)
    
print(new_item)
    
       
    
     
    