# TC: O(N)
# SC: O(K)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        cnt_s = Counter(s)
        cnt_t = Counter(t)

        return cnt_s == cnt_t

