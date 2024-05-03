class MyStack:
    
    def __init__(self, size):
        self.stack = []
        self.size = size
        
    def push(self, value):
        if len(self.stack) < self.size:
            self.stack.append(value)
        else:
            print("Stack is full")
            
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.size
