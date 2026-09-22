class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_parenthesis_map = {
            "[": "]",
            "(": ")",
            "{": "}"
        }

        for ch in s:
            if ch in close_parenthesis_map:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if close_parenthesis_map[top] != ch:
                    return False

        if len(stack) > 0:
            return False

        return True
