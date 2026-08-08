# TC: O(N)
# SC: O(K)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx_map = {}
        start = 0
        ans = 0

        for end in range(len(s)):
            c = s[end]
            if c in idx_map and start <= idx_map[c]:
                start = idx_map[c] + 1
            else:
                ans = max(ans, end - start + 1)

            idx_map[c] = end

        return ans

