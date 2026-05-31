class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """격자에서 (0, 0) 위치에서 시작해 (m-1, n-1) 위치에 도달하는 경로의 수를 구하는 함수
        
        방법:
        1. 최적의 경로 -> DP 문제!
            - 각 위치에서는 오른쪽과 아래로만 가지 못함
            - 따라서, dp[i][j] = dp[i - 1][j] + dp[i][j - 1]로 표현 가능
        시간 복잡도: O(m*n) - 모든 위치에 대해 계산하는 경우
        공간 복잡도: O(m*n) - dp 테이블을 저장하는 경우

        Args:
            m (int): 격자의 행 갯수
            n (int): 격자의 열 갯수

        Returns:
            int: (m-1, n-1) 위치에 도달하는 경로의 수
        """
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
