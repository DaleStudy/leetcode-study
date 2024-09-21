"""TC: O(n), SC: O(n)

문자열 길이 n

아이디어:
- 문자열을 앞에서부터 훑으면서
    - 괄호 시작을 발견하면 스택에 넣는다.
    - 괄호 끝을 발견하면 스택의 제일 마지막에 있는 아이템을 pop해서 매칭이 되는지 확인한다.
- 이때 다음과 같은 예외 상황들을 조심한다.
    - 스택에 아이템이 하나도 없는데 pop을 하려는 상황 방지.
        - e.g.) "))))"
    - 모든 문자열을 훑고 지나갔는데 스택에 아이템이 남아있는 경우도 실패다.
        - e.g.) "(((("

SC:
- 시작 괄호 리스트 O(1).
- 끝 괄호와 매칭되는 시작 괄호 dict O(1).
- 시작 괄호만 있는 경우 스택에 쌓이는 아이템은 총 n개다. O(n).
- 종합하면 O(n).

TC:
- 문자 총 n개에 대해 아래를 반복한다.
    - 시작 괄호인지 체크. O(1).
    - 시작 괄호인 경우 스택에 쌓기 O(1).
    - 끝 괄호인 경우 스택에서 pop할때 O(1), 괄호 매칭 체크시 O(1).
- 종합하면 O(n).
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = ["(", "{", "["]
        ending_match = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for c in s:
            if c in openings:
                stack.append(c)
            else:
                if not stack or ending_match[c] != stack.pop():
                    return False
        return False if stack else True
