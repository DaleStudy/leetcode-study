# 1) Sort input strings and check if those are the same.
# TC: O(NlogN) where N is the size of string s and t due to sorting
# SC: O(N) where N is the length of string s and t to store sorted list.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# 2) Using dict to store count of the first string and decrease back to see if there's negative count.
# TC: O(N + M) where N is the length of s and M is the length of t.
# SC: O(N + M) where N is the length of s and M is the length of t.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        char_map: Dict[str, int] = {}
        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1

        for ch in t:
            if ch not in char_map or char_map[ch] == 0:
                return False

            char_map[ch] -= 1

        return True
