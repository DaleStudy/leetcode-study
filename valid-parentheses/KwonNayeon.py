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

풀이방법:
1. 스택을 사용하여 여는 괄호('(', '{', '[')를 저장
2. Dictionary를 사용해 닫는 괄호와 여는 괄호의 쌍을 O(1)로 매칭
3. 문자열을 순회하면서:
   - 여는 괄호는 스택에 추가
   - 닫는 괄호가 나오면:
     a) 스택이 비어있거나
     b) 스택 최상단의 괄호가 현재 닫는 괄호와 매칭되지 않으면
     -> 잘못된 괄호 문자열
   - 매칭되는 경우 스택에서 pop
4. 모든 순회가 끝난 후 스택이 비어있어야 올바른 괄호 문자열
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
