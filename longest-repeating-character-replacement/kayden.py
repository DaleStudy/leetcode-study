from collections import defaultdict

class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(N)
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        l, r = 0, 1

        d = defaultdict(int)
        d[s[l]] += 1

        longest = 1
        while l < r and r < n:
            d[s[r]] += 1
            if r-l+1 - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
            r += 1

        return longest
