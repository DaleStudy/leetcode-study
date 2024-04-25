"""
https://leetcode.com/problems/valid-palindrome/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in s if i.isalnum()]).lower()
        return s == s[::-1]
