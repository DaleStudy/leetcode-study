"""
복잡도:
    n: `s`의 길이
    시간 복잡도: O(n)
    공간 복잡도: O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # 괄호 개수가 짝수인 경우는 항상 실패
        if len(s) % 2:
            return False
    
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []
        
        for char in s:
            if char in brackets: # 닫히는 괄호인지
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return len(stack) == 0
