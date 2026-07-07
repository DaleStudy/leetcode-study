# TC: O(N)
# SC: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        import re

        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        n = len(s)

        for idx in range(0, n // 2):
            if s[idx] != s[n - idx - 1]:
                return False

        return True

