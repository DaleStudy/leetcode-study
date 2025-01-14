"""
Constraints:
1. 1 <= s.length <= 10^4
2. s consists of parentheses only '()[]{}'

Time Complexity: O(n)
- 문자열의 각 문자를 한 번씩만 순회하므로 O(n)
- 각 문자에 대한 연산(push, pop)은 O(1)

Space Complexity: O(n)
- 최악의 경우 모든 문자가 여는 괄호일 때 스택에 모두 저장
- 따라서 입력 크기에 비례하는 O(n) 공간 필요
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0
