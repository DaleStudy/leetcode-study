"""
https://leetcode.com/problems/valid-anagram/
"""
# - time complexity : O(n)
# - space complexity : O(n)

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
