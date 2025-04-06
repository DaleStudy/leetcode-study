class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        count = [0] * 26
        for ch_s, ch_t in zip(s, t):
            count[ord(ch_s) - ord('a')] += 1
            count[ord(ch_t) - ord('a')] -= 1
        return all(x == 0 for x in count)
