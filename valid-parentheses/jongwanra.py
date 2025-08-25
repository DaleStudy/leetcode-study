"""
[Problem]
https://leetcode.com/problems/valid-parentheses/

[Brainstorming]
1. 여는 괄호가 나올 경우에 Stack에 Push한다.
2. 닫는 괄호가 나왔을 경우에 Stack 가장 위에 여는 괄호와 일치 여부를 확인한다.

이렇게 했을 때, 시간 복잡도는 O(N)으로 예상한다. (여기서 N은  s.length)

[Complexity]
Time: O(N), N = s.length
Space: O(N), N = stack.length
"""
from os import popen


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {'(':')', '{':'}', '[':']'}
        stack = []
        for bracket in s:
            # 여는 괄호인 경우 Stack 추가
            if bracket in bracket_dict:
                stack.append(bracket)
                continue

            # 닫는 괄호인 경우
            if not stack or bracket_dict[stack.pop()] != bracket:
                return False

        return not stack

sol = Solution()

# Normal Case
print(sol.isValid("()") == True)
print(sol.isValid("()[]{}") == True)
print(sol.isValid("(]") == False)
print(sol.isValid("([])") == True)
print(sol.isValid("([)]") == False)

# Edge Case
print(sol.isValid("(") == False)
print(sol.isValid("]") == False)

