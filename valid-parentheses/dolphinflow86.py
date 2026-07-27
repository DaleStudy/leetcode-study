# 1) While iterating through string s, push open brackets onto the stack; otherwise check if the current bracket is paired with top of the stack. If paired, pop top of stack; otherwise, return false. After iteration, return true if stack is empty; otherwise return false.
# TC: O(N) where N is the len(s)
# SC: O(N) where N is the len(s)
class Solution:
    def is_pair(self, open_bracket, close_bracket):
        return ((open_bracket == '(' and close_bracket == ')') or
            (open_bracket == '{' and close_bracket == '}') or
            (open_bracket == '[' and close_bracket == ']'))
            
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif stack and self.is_pair(stack[-1], ch):
                stack.pop()
            else: return False
            
        return not stack
