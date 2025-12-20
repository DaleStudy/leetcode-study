class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1
    
    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else:
            pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else:
            pass

class Solution:
    def isValid(self, s: str) -> bool:
        stack = ArrayStack(100)
        for ch in s:
            if ch in ('(', '[', '{'):
                stack.push(ch)
            elif ch in (')', ']', '}'):
                if stack.isEmpty():
                    return False
                else:
                    left = stack.pop()
                    if (ch == ')' and left != '(') or \
                       (ch == ']' and left != '[') or \
                       (ch == '}' and left != '{'):
                           return False
        return stack.isEmpty()


