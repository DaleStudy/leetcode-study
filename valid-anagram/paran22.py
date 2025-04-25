from collections import Counter

class Solution:
    # time complexity: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
