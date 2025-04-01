"""
O(n) complexity
"""
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ["(", "{", "["]
        bracket_map = {"(":")", "{":"}", "[":"]"}
        stack = []
        for char in s:
            if char in open_brackets:
                stack.append(char)
                continue
            if not stack: # no matching open bracket for char
                return False
            open_b = stack.pop() # last in open bracket
            if bracket_map[open_b] != char: # dismatch between open b and close b
                return False
        if stack: # open bracket remaining
            return False
        return True
            
        