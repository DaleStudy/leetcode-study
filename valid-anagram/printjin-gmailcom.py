from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str):
        return Counter(s) == Counter(t)
