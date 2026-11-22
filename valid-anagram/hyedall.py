"""
# https://leetcode.com/problems/valid-anagram/description/

시간 복잡도 : O(n)
공간 복잡도 : O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            count[c] = count.get(c, 0) - 1

            if count[c] < 0:
                return False
        
        return True

