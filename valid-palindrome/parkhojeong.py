class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_str = ""
        for ch in s:
            if ch.isalnum():
                normalized_str += ch.lower()

        return normalized_str == normalized_str[::-1]
