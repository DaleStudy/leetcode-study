class Solution:
    def isValid(self, s: str) -> bool:
        characters_dict = {')': '(', '}': '{', ']': '['}

        stack = []
        for ch in s:
            if ch in characters_dict.values():
                stack.append(ch)
            elif ch in characters_dict:
                if not stack or stack[-1] != characters_dict[ch]:
                    return False
                stack.pop()

        return not stack

