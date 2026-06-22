import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return result == result[::-1]
