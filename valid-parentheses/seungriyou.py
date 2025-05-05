# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            s를 순회하면서 다음을 stack에 수행한다.
                - 닫는 괄호: stack이 비어있거나, stack.top이 매칭이 안 된다면 빠르게 False 반환 (+ 매칭이 된다면 stack.pop())
                - 여는 괄호: stack에 추가
            이렇게 전체를 순회했을 때 stack이 비어있어야 valid parentheses이다.
        """

        matches = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for p in s:
            # 닫는 괄호: (1) stack이 비어있거나 (2) stack의 top이 pair가 아니라면 False (+ pair라면 stack.pop())
            if p in matches:
                if not stack or stack.pop() != matches[p]:
                    return False
            # 여는 괄호: stack에 추가
            else:
                stack.append(p)

        # stack이 비어있어야 valid parentheses
        return not stack
