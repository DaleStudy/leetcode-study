# O(s) 공간 복잡도 : 입력문자열 s 길이에 따라 최대 s 깊이의 stack 생성
# O(s) 시간 복잡도 : 문자열 s 길이에 따라 for문 반복
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'[': ']', '(': ')', '{': '}'}

        for i, ch in enumerate(s):
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                # '(', '[', '{' 문자가 앞에 없이 ')', ']', '}' 문자가 오는 경우
                if not stack:
                    return False
                lastCh = stack.pop()
                # pair가 맞지 않는 문자인 경우
                if pairs[lastCh] != ch:
                    return False
        # stack에 값이 비지 않은 경우, pair가 맞지 않음
        return not stack
