'''
시간 복잡도: O(m * n)
- 동적 프로그래밍 테이블(dp)을 사용하여 각 셀에서의 경로 수를 한 번씩 계산하므로 시간 복잡도는 격자의 모든 셀에 대해 O(m * n)입니다.

공간 복잡도: O(m * n)
- dp 테이블을 사용하여 모든 셀에 대한 경로 수를 저장하므로 공간 복잡도는 O(m * n)입니다.
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # save number of unique paths to each cell
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
                
        return dp[m - 1][n - 1]
