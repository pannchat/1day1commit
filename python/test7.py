class Stack:
    def __init__(self):
        self.top = 0
        self.arr = [0]*4
    def push(self, value):
        self.top += 1
        self.arr[self.top] = value
    
    def pop(self):
        value = self.arr[self.top]
        self.top -= 1
        return value

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop(), end='')
print(stack.pop(), end='')
print(stack.pop(), end='')
