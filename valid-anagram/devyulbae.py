"""
Blind 75 - LeetCode Problem 242: Valid Anagram
https://leetcode.com/problems/valid-anagram/

t가 s의 애너그램인지 확인하기
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

