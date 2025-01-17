class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = dict(zip('({[',')}]'))
        for paren in s :
            if paren in pair :
                stack.append(paren)
            elif not stack :
                return False
            elif pair[stack[-1]] == paren :
                stack.pop()
            else:
                return False
        if not stack :
            return True
        else :
            return False