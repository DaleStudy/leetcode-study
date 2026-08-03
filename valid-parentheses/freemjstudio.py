class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']
        stack = []
        if len(s) == 1:
            return False

        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
            else: # ]
                if not stack:
                    return False
                top = stack.pop()
                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False
        if len(stack) > 0:
            return False
        return True
