"""
Time Complexity: O(n)
    - Each character in the input string s is visited exactly once in a single left-to-right scan.
    - Each push or pop operation on the stack corresponds to a character, for at most O(n) stack operations.

Space Complexity: O(n)
    - In the worst case (e.g., all opening brackets), the stack may contain up to n elements.
    - The auxiliary data structure (`pairs`) uses constant space, as there are only three types of parentheses.

Approach:
    The algorithm uses a stack to simulate balancing of brackets.
    - For every opening bracket encountered, push it onto the stack.
    - For every closing bracket, check if the top of the stack holds its matching opening bracket.
      - If not, or if the stack is empty, the string is invalid.
    - At the end, if the stack is empty, all open brackets were matched and closed properly.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif not stack or pairs[stack[-1]] != ch:
                return False
            else:
                stack.pop()

        return not stack
