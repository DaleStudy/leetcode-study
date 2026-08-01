class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {"()", "{}", "[]"}

        for char in s:
            stack.append(char)
            if len(stack) >= 2:
                if ''.join(stack[-2:]) in map:
                    stack.pop()
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False        
