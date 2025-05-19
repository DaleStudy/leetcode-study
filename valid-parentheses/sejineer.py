"""
시간 복잡도: O(N)
공간 복잡도: O(N)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if stack:
                    cur = stack.pop()
                    if pair[cur] == c:
                        continue
                    else:
                        return False
                else:
                    return False
        return not stack
