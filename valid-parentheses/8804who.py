class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)

        while s:
            if s[-1] in [')', '}', ']']:
                stack.append(s[-1])
            elif s[-1] == '(':
                if not stack or stack.pop() != ')':
                    return False
            elif s[-1] == '{':
                if not stack or stack.pop() != '}':
                    return False
            else:
                if not stack or stack.pop() != ']':
                    return False
            s.pop()
            
        return False if stack else True
    
