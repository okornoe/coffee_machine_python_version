class Stack():

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        if len(self.stack) >= 1:
            return self.stack.pop(len(self.stack) - 1)

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        return self.stack == []
