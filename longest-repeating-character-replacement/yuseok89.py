# TC: O(N)
# SC: O(K)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        cnt = defaultdict(int)
        m, ans = 0, 0

        for r in range(len(s)):
            c = s[r]
            cnt[c] += 1

            m = max(m, cnt[c])

            while m + k < r - l + 1:
                c = s[l]
                l += 1
                cnt[c] -= 1

                if cnt[c] == m - 1:
                    m = max(cnt.values())

            ans = max(ans, r - l + 1);

        return ans

