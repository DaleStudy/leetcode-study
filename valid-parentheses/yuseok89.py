# TC: O(N)
# SC: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        pars = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c in pars:
                stack.append(c)
            else:
                if not stack or pars[stack.pop()] != c:
                    return False

        return len(stack) == 0

