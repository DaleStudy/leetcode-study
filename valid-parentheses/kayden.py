# 시간복잡도: O(N)
# 공간복잡도: O(1)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        matching_brackets = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in matching_brackets:
                stack.append(char)
            elif stack and matching_brackets[stack[-1]] == char:
                stack.pop()
            else:
                return False

        return not stack
