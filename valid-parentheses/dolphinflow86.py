# 1) While iterating through string s, push open brackets onto the stack; otherwise check if the current bracket is paired with top of the stack. If paired, pop top of stack; otherwise, return false. After iteration, return true if stack is empty; otherwise return false.
# TC: O(N) where N is the len(s)
# SC: O(N) where N is the len(s)
class Solution:

    def isValid(self, s: str) -> bool:
        pair = {
                '(': ')',
                '[': ']',
                '{': '}',
            }
        
        stack = []

        for ch in s:
            if ch in pair:
                stack.append(ch)
            elif stack and pair[stack[-1]] == ch:
                stack.pop()
            else: return False
            
        return not stack
