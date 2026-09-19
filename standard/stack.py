class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop(-1) if self.stack else None

    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i])