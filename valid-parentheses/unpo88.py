class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)

        return not stack


"""
================================================================================
풀이 과정
================================================================================

[1차 시도] Stack으로 직접 비교
────────────────────────────────────────────────────────────────────────────────
1. 괄호 판독기
2. Stack으로 괄호 넣고, 매칭되는것이 나왔을 때, 바로 pop하면서 비교
3. 하나라도 틀린게 있으면 False
4. 아니면 True

        stack = []
        for c in s:
            if c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            else:
                stack.append(c)

        return True if len(stack) == 0 else False

5. 문제점: 각 닫는 괄호마다 동일한 패턴이 반복됨
6. 개선 포인트: 딕셔너리로 매핑하면 중복 제거 가능

────────────────────────────────────────────────────────────────────────────────
[2차 시도] 딕셔너리 매핑으로 개선
────────────────────────────────────────────────────────────────────────────────
7. pairs = {')': '(', '}': '{', ']': '['}
   - 닫는 괄호 → 여는 괄호 매핑

8. 개선된 로직:
   - c가 닫는 괄호면 (c in pairs) → stack에서 pop해서 매칭 확인
   - c가 여는 괄호면 → stack에 push

        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)

        return not stack

9. 추가 개선:
   - len(stack) == 0 → not stack 
   - True if ... else False → not stack

10. 시간복잡도: O(n) - 문자열 한 번 순회
11. 공간복잡도: O(n) - 최악의 경우 모든 문자가 여는 괄호
"""
