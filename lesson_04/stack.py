class StackBase(list):

    def __init__(self):
        super().__init__()

    def size(self):
        return len(self)

    def push(self, n):
        self.append(n)

    def pop(self):
        return super().pop()

    def top(self):
        return self[-1]

    def empty(self):
        return self.size() == 0

    def clear(self):
        super().clear()

    def __str__(self):
        return super().__str__()


stack = StackBase()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
stack.pop()
print(stack)
print(stack.empty())
print(stack.top())
print(stack.size())
