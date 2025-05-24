class Solution:
    def isValid(self, s: str) -> bool:
        
        # Stack
        stack = []
        i = 0

        while i < len(s):
            # 여는 괄호일 경우 스택에 추가
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            
            # 닫는 괄호일 경우 
            else:
                # 스택이 비어 있을경우 짝이 맞지않으므로 False 리턴
                if not stack:
                    return False

                # 스택 마지막에 짝맞는 여는 괄호가 없으면 False
                if s[i] == ")" and stack[-1] != "(":
                    return False
                elif s[i] == "}" and stack[-1] != "{":
                    return False 
                elif s[i] == "]" and stack[-1] != "[":
                    return False
                    
                # 짝이 맞으면 pop
                stack.pop()

            # 다음 글자로 이동
            i += 1

        # 문자열을 다 돌고, 스택도 비어있다면 True 리턴
        return not stack
