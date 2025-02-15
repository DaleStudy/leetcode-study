"""
Solution:
    1) s 를 순회하면서 여는 괄호면 stack 에 push 한다.
    2) 닫는 괄호일 경우 각 case 별로 stack 의 최상단이 알맞는 여는 괄호이면 stack 을 pop 하고 아니면 False 를 return 한다.
Time: O(n)
Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ["(", "{", "["]
        for char in s:
            if char in left:
                stack.append(char)
                continue

            if not stack:
                return False

            if char == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            if char == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            if char == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        return not stack


"""
Solution:
    1) stack과 hash map을 사용한다.
    2) s를 순회하면서 여는 괄호일 경우 stack 에 push
    3) 닫는 괄호일 경우 stack 이 비지 않으면서 최상단 요소가 알맞은 여는 괄호이면 stack pop, 아닐 경우 return False
    
Time: O(n)
Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        opening = "({["
        closing = ")}]"
        closeToOpen = dict(zip(closing, opening))

        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
        return not stack
