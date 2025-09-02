class Solution:
    """
    1. 스택을 활용한 분기 처리
    여는 괄호일 때는 스택에 무조건 넣어준다.
    닫는 괄호일 때는 대, 중, 소 괄호에 맞춰서 분기를 해줘야 한다.
    스택이 있고, 스택의 마지막이 해당 괄호의 여는 괄호이면 빼내준다.
    이외는 닫힌 괄호가 먼저 나오는 것이기 때문에 False를 반환해준다.
    전형적인 스택 문제로 O(n)의 시간복잡도를 가진다.
    """
    def isValid(self, s: str) -> bool:
        stack = []
        for word in s:
            if word == "(" or word == "{" or word == "[":
                stack.append(word)
            elif stack and word == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and word == "]" and stack[-1] == "[":
                stack.pop()
            elif stack and word == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return True if not stack else False
