from math import comb
class Solution:
    # 시간복잡도: O(m+n)
    # 공간복잡도: O(1)
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2, n-1) # m+n-2Cn-1

    # 시간복잡도: O(m*n)
    # 공간복잡도: O(n)
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]

        return dp[n-1]
