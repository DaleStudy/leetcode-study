"""
Time complexity O(n)
Space complexity O(n)
"""
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = defaultdict(int)
        t_cnt = defaultdict(int)
        for char in s:
            s_cnt[char] += 1
        for char in t:
            t_cnt[char] += 1
        if s_cnt != t_cnt:
            return False
        return True    
