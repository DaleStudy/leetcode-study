"""
Constraints:
    - 1 <= len(s), len(t) <= 50_000
    - s and t consist of lowercase English letters (a-z) only

Time Complexity:
    - O(n log n)
Space Complexity:
    - O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = s.replace(' ', '').lower()
        t = t.replace(' ', '').lower()

        if sorted(s) == sorted(t):
            return True
        else:
            return False
