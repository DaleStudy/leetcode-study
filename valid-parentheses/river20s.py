class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, element):
        self.data.append(element)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return None
# <<<--- Stack 구현 ---<<<
# >>>--- 답안 Solution --->>>
class Solution:
    # 스택을 활용해 괄호 유효 검사
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def __init__(self):
        self._opening_brackets = '([{'
        self._closing_brackets = ')]}'
        self._matching_map = {')': '(', ']': '[', '}': '{'}

    def isValid(self, s: str) -> bool:
        stack = Stack()
        for char in s:
            # 여는 괄호라면 스택에 push
            if self._is_opening(char):
                stack.push(char)
            # 닫는 괄호라면
            # 마지막 열린 괄호와 유형 일치 확인
            elif self._is_closing(char):
                if stack.is_empty():
                    # 스택이 비어 있으면 False 반환
                    return False
                last_open_bracket = stack.pop()
                if not self._is_match(last_open_bracket, char):
                    return False
        return stack.is_empty()

    def _is_opening(self, char: str) -> bool:
        return char in self._opening_brackets

    def _is_closing(self, char: str) -> bool:
        return char in self._closing_brackets

    def _is_match(self, open_bracket: str, close_bracket: str) -> bool:
        return self._matching_map.get(close_bracket) == open_bracket 
