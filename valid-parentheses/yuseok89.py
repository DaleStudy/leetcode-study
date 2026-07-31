# TC: O(N)
# SC: O(N/2)
class Solution:
    def isValid(self, s: str) -> bool:
        pars = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c in pars:
                stack.append(c)
            else:
                if len(stack) == 0 or pars.get(stack.pop(), '') != c:
                    return False

        return len(stack) == 0

