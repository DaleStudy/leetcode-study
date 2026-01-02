# 시간 복잡도: O(n)
# - s의 길이만큼 탐색하기 때문에
# 공간 복잡도: O(n)
# - stack을 list로 사용하며 s[:-1]까지 모든 다른 왼쪽 괄호일 때 O(n)까지 늘어날 수 있음

class Solution:
    # 왼쪽 괄호는 stack에 저장하고 오른쪽 괄호가 들어왔을 때,
    # stack의 가장 마지막에 들어온 왼쪽 괄호와 쌍이 맞는지 확인하여
    # 모든 경우에 쌍이 맞으면 이 문자열이 valid하다고 할 수 있다.
    # 만약 유효성에서 falsy한 경우에는 early return 해준다.
    def isValid(self, s: str) -> bool:
        stack = []

        for ss in s:
            if ss in ('(', '[', '{'):
                # 왼쪽 괄호는 stack에 저장
                stack.append(ss)
            else:
                # 오른쪽 괄호는 stack 내부 요소를 확인하여 유효성 확인
                if not stack:
                    # stack이 없는 경우에는 쌍을 맞출 왼쪽 괄호가 없으므로 s가 invalid하다고 할 수 있음
                    return False

                # stack의 마지막 요소와 현재 확인할 문자열의 쌍이 맞는지 확인
                last_ss = stack[-1]
                if any([
                    last_ss == '(' and ss == ')',
                    last_ss == '[' and ss == ']',
                    last_ss == '{' and ss == '}',
                ]):
                    # 쌍이 맞다면 stack의 마지막 문자열은 pop
                    stack.pop()
                else:
                    # 쌍이 안 맞는 경우
                    return False
        if stack:
            # 모든 문자열을 돌았는데도, stack에 왼쪽 괄호가 남아 있는 경우
            return False
        
        # 위의 모든 invalid한 경우를 통과했다면 valid하다고 할 수 있다.
        return True

    # 리뷰 반영 풀이
    # 괄호의 쌍을 key-value로 하는 pairs 딕셔너리를 이용하여, if 조건을 더욱 간단하게 할 수 있음
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for ss in s:
            if ss in ('(', '[', '{'):
                stack.append(ss)
            else:
                if not stack:
                    return False

                last_ss = stack[-1]
                if last_ss == pairs[ss]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
