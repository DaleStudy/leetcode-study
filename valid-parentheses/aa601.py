class Solution:
    def isValid(self, s: str) -> bool:
        # stack 활용, 짝이 맞으면 pop하기
        stack = []
        dic = dict(zip(")}]", "({[")) # close bracket : open bracket 형태로 사전 생성
        for char in s:
            if char in "({[": # open bracket인 경우 stack에 추가
                stack.append(char)
            elif char in ")}]" : # close bracket이면서
                if not stack or stack.pop() != dic[char]: 
                    return False

        # len()함수 시간복잡도 먹음 O(n)
        # => not stack 사용하면 개선됨
        if len(stack) == 0: # stack이 비어있다면 모든 짝이 맞아서 pop되었으므로 true 반환 
            return True
        else:
            return False
