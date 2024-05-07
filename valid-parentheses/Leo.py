class Solution:
    def isValid(self, s: str) -> bool:

        d = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False

        return len(stack) == 0

        ## O(n) time complexity but not that much fast by leetcode system...
        ## Space complexity is also O(n)
