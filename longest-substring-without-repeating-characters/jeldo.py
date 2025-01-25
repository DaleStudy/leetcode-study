class Solution:
    # O(n), n = len(s)
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        chars = dict()
        l = 0
        for r in range(len(s)):
            if s[r] not in chars or chars[s[r]] < l:
                chars[s[r]] = r
                max_len = max(max_len, r - l + 1)
            else:
                l = chars[s[r]] + 1
                chars[s[r]] = r
        return max_len
