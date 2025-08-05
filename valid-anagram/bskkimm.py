from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram is a word formed by rearranging each letter of a word exactly once.
        # s = "anagram", t = "nagaram"
        return Counter(s) == Counter(t)
