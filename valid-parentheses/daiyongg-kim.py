class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                
                cur = stack.pop()
                if cur == '(' and c != ')':
                    return False
                if cur == '{' and c != '}':
                    return False
                if cur == '[' and c != ']':
                    return False
        if not stack:
            return True
        else:
            return False