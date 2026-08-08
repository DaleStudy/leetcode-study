# TC: O(NM)
# SC: O(N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cnt = [0] * n
        cnt[0] = 1

        for i in range(0, m):
            for j in range(1, n):
                cnt[j] += cnt[j - 1]

        return cnt[n - 1]

