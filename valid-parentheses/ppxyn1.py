# idea : stack

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:
            if ch in mapping:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if mapping[stack.pop()] != ch:
                    return False
        if stack:
            return False

        return True


    
