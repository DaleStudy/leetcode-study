class Solution:
    def isValid(self, s: str) -> bool:
        """
        - Idea: 주어진 문자열을 순회하면서 여는 괄호는 스택에 넣고, 닫는 괄호는 스택의 최상단 요소와 매칭되는지 확인한다.
        - Time Complexity: O(n), n은 주어진 문자열의 길이. 모든 문자를 한번씩은 순회한다.
        - Space Complexity: O(n), 주어진 문자열이 모두 여는 괄호일 경우 스택에 저장된다.
        """
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for char in s:
            if char in bracket_map:
                stack.append(char)
            elif not stack or bracket_map[stack.pop()] != char:
                return False

        return not stack
