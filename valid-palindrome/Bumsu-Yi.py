"""
https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_chars = []
        for char in s:
            if char.isalnum():
                lowercase_letter = char.lower()
                alphanumeric_chars.append(lowercase_letter)

        return alphanumeric_chars == alphanumeric_chars[::-1]
