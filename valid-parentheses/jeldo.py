class Solution:
    # O(n), n = len(s)
    def isValid(self, s: str) -> bool:
        parentheses = {
            "(": ")",
            "]": "]",
            "{": "}",
        }
        stack = []
        for ch in s:
            if ch in parentheses.keys():
                stack.append(ch)
            elif stack and ch == parentheses[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
