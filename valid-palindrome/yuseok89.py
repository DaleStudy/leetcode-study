# TC: O(N)
# SC: O(1)
class Solution:

    def is_alphanum(self, c):
        return 'a' <= c <= 'z' or '0' <= c <= '9'

    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        s = s.lower()

        while(left < right):
            while left < len(s) and not self.is_alphanum(s[left]):
                left += 1
            while right >= 0 and not self.is_alphanum(s[right]):
                right -= 1

            if left < right and s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#
#         import re
#
#         s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
#
#         n = len(s)
#
#         for idx in range(0, n // 2):
#             if s[idx] != s[n - idx - 1]:
#                 return False
#
#         return True

