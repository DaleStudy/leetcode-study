"""
Problem : Valid Parentheses
유형 : 스택
문제 해석
* 괄호 문자열이 올바르게 짝지어져 있는지 판단
* 3가지 종류의 괄호: (), {}, []
* 여는 괄호는 같은 종류의 닫는 괄호로 닫혀야 함
* 괄호는 올바른 순서로 닫혀야 함

해결 전략
스택 자료구조를 활용한다.
* 여는 괄호를 만나면 스택에 push
* 닫는 괄호를 만나면 스택의 top과 매칭 확인
  * 스택이 비어있으면 → 매칭되는 여는 괄호가 없음 (False)
  * top과 종류가 다르면 → 잘못된 순서 (False)
  * 매칭되면 → pop으로 제거
* 모든 처리 후 스택이 비어있어야 올바른 괄호열

구현
딕셔너리로 닫는 괄호와 여는 괄호의 매칭 관계를 정의한다.
* matching = {')': '(', '}': '{', ']': '['}
* 닫는 괄호를 key로 사용하여 O(1)에 매칭 확인 가능

주의할 점
* 여는 괄호만 있는 경우 → 스택에 남아있으므로 False
  예: "(((" → stack = ['(', '(', '(']
* 닫는 괄호만 있는 경우 → 스택이 비어있어서 False
  예: ")))" → stack이 비어있음
* 순서가 잘못된 경우 → 매칭 실패로 False
  예: "([)]" → ']'를 처리할 때 top이 '['인데 ')'를 기대
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 닫는 괄호 : 여는 괄호 매핑
        matching = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching:  # 닫는 괄호인 경우
                # 스택이 비어있거나 매칭 안되면 False
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()  # 매칭 성공시 제거
            else:  # 여는 괄호인 경우
                stack.append(char)  # 스택에 추가

        # 모든 괄호가 매칭되었으면 스택이 비어있어야 함
        return len(stack) == 0
