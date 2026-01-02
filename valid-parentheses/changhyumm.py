class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        # 괄호의 특성상 stack 자료구조 활용
        # 시간 복잡도 O(n)
        # 공간 복잡도 O(n)
        for string in s:
            if string not in brackets:
                if len(stack) == 0:
                    return False
                else:
                    target = stack.pop()
                    if string != target:
                        return False
            else:
                stack.append(brackets[string])
        if stack:
            return False
        return True
