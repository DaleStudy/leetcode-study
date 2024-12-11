class Solution:
    # O(n)
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())  # O(n)
        return s == s[::-1]  # O(n)
