class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        res = 0

        for right, curr in enumerate(s):
            if curr in seen:
                left = max(left, seen[curr] + 1)
            res = max(res, right - left + 1)
            seen[curr] = right

        return res

        ## TC:O(n), SC:O(min(m,n)) where n is len(s) and m is size(seen)
