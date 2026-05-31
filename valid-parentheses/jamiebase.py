"""
# Approach
스택을 이용하여 닫는 괄호가 나올 때 스택 top과 비교하여 짝이 맞으면 pop합니다.
짝이 맞지 않으면 invalid, 최종적으로 스택이 비어있지 않으면 invalid 합니다.

# Complexity
s의 길이를 N이라고 할 때
- Time complexity: O(N)
- Space complexity: O(N)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for b in s:
            if b in brackets:
                stack.append(b)
                continue
            if not stack or brackets[stack.pop()] != b:
                return False
        return not stack
