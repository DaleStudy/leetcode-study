from collections import deque


class Solution:
    # Time Complexity: O(n), n: len(s)
    # Space Complexity: O(n), n: len(s)
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = deque()

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif len(stack) != 0:
                top = stack.pop()
                if (top == '(' and ch == ')') or (top == '[' and ch == ']') or (top == '{' and ch == '}'):
                    continue
                else:
                    return False
            else:
                return False

        return len(stack) == 0
