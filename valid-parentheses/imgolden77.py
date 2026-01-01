# First try O(n) time complexity
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        former= ['(', '{', '[']
        
        for i in s:
            if i in former:
                stack.append(i)
            elif i == ')':
                if stack== []:
                    return False
                elif stack[-1]== '(':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if stack== []:
                    return False
                elif stack[-1]== '{':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                if stack == []:
                    return False
                elif stack[-1]== '[':
                    stack.pop()
                else:
                    return False
            
        
        if stack == []:
            return True
        else:
            return False
        
# Second try: O(n) time complexity
# refer other people's code 
# 'not stack' is more pythonic way to check empty stack
# par_map dictionary to map closing to opening parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {')':'(', '}':'{', ']':'['}
        
        for i in s:
            if i in par_map.values():
                stack.append(i)
            elif i in par_map:
                if not stack or stack[-1] !=par_map[i]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack
    

