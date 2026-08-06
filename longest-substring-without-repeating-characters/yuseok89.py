# TC: O(N)
# SC: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        l, r = 0, 0

        for r in range(0, len(s)):
            c = s[r]

            while c in seen:
                seen.remove(s[l])
                l += 1

            seen.add(c)

            ans = max(ans, r - l + 1)

        return ans

