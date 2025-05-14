class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # DP (시간복잡도 O(m*n), 공간복잡도 O(m*n))
        # 모든 1행과 1열은 경로가 1개이므로 1로 배열 초기화.
        dp = [[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                # 현재위치 경로 경우의 수 = 위쪽 + 왼쪽
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
