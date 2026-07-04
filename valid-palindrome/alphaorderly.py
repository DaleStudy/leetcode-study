class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = "".join(ch.lower() for ch in s if ch.isalnum())

        return processed == processed[::-1]