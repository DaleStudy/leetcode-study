'''
문제: 괄호 쌍 유효성 검사(서로 엇갈려서 짝이 맞으면 무효함)
풀이: 스택 자료구조를 활용하여 여는 괄호를 만나면 스택에 추가, 닫는 괄호를 만나면 스택의 최상단 요소와 비교하여 짝이 맞으면 pop, 아니면 False 반환
시간복잡도: O(n)
공간복잡도: O(n)
사용한 자료구조: 스택(리스트)
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if len(stack) == 0 and (i == '}' or i == ')' or i == ']'):
                return False
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            if i == '}' or i == ')' or i == ']':
                if i == '}' and stack[len(stack)-1] == '{':
                    stack.pop()
                elif i == ')' and stack[len(stack)-1] == '(':
                    stack.pop()
                elif i == ']' and stack[len(stack)-1] == '[':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
    


