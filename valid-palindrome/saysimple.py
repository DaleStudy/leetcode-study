"""
https://leetcode.com/problems/valid-palindrome/
"""
# - time complexity : O(n)
# - space complexity : O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in s if i.isalnum()]).lower()
        return s == s[::-1]
