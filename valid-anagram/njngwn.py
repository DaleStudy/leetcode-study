from collections import Counter

class Solution:
    # Time Complexity: O(n), n: max(len(s), len(t))
    # Space Complexity: O(k), k: number of letters
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
