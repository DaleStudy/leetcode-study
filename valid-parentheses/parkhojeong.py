class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_parenthesis_set = set({"{", "[", "("})
        close_parenthesis_map = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        for ch in s:
            if ch in open_parenthesis_set:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if close_parenthesis_map[ch] != top:
                    return False

        if len(stack) > 0:
            return False

        return True
