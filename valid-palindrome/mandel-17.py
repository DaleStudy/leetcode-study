class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = [c.lower() for c in s if c.isalnum()]
        return ch == ch[::-1]
    