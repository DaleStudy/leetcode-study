"""
 * Time Complexity: O(n)
 * Space Complexity: O(n)
"""
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = Counter(s)
        for c in t:
            s_dict[c] -= 1
            if s_dict[c] < 0:
                return False

        return True
