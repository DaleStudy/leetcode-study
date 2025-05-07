"""
Time complexity O(n)

stack
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
            if not stack:
                return False
            open_b = stack.pop() # last in open bracket
            if bracket_map[open_b] != char:
                return False
        if stack:
            return False
        return True
            
        