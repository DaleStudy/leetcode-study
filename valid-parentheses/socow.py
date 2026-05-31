class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 ==1:
            return False
        
        pair = {")":"(","}":"{","]":"["}
        all = set(pair.values())
        stack = []

        for x in s:
            if x in all:
                stack.append(x)
            else:
                if not stack or stack[-1] !=pair[x]:
                    return False
                stack.pop()
        return not stack
