'''
20. Valid Parentheses
Stack을 사용하는 문제임을 파악하지 못해서 결국 알고달레님의 도움을 받았습니다. 

Time Complexity: O(n)
Space Complexity: O(n)
'''
class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for val in s:
            if val in parens:
                stack.append(val)
            else:
                if not stack or val != parens[stack.pop()]:
                    return False
        return not stack
