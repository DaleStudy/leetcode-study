# 1) Sort input strings and check if those are the same.
# TC: O(NlogN) where N is the size of string s and t due to sorting
# SC: O(N) where N is the length of string s and t to store sorted list.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
