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
- key: 닫는 괄호, value: 대응하는 여는 괄호
- 현재 문자가 닫는 괄호인 경우
  - 스택이 비어있다면(짝이 없음) -> False
  - 스택에서 가장 최근에 추가된 여는 괄호를 꺼냄, 만약 대응하는 값이 아니라면 -> False
- 현재 문자가 여는 괄호인 경우 -> stack에 추가
- 모든 문자 처리 후, 스택이 비어있으면 모든 괄호의 짝이 맞음 (True)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack:
                    return False
                
                top = stack.pop()

                if mapping[char] != top:
                    return False
            
            else:
                stack.append(char)

        return not stack
