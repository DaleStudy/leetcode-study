'''
시간 복잡도: O(n)
- 문자열 s의 길이를 n이라고 할 때, 문자열의 각 문자를 한 번씩 순회하며 처리하므로 O(n)입니다.

공간 복잡도: O(n)
- 스택에 열린 괄호를 저장하는 데 사용되는 공간이 최악의 경우 문자열 s의 길이 n과 같을 수 있으므로 O(n)입니다.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in bracket_map:
                if stack and stack[-1] == bracket_map[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 0
