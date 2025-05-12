# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths_2d(self, m: int, n: int) -> int:
        """
        [Complexity]
            - TC: O(m * n)
            - SC: O(m * n)

        [Approach]
            로봇이 down or right로만 이동할 수 있으므로, 어떤 칸에 도달할 수 있는 unique path의 개수는 up 칸과 left 칸까지의 unique path의 개수를 더한 값이 된다.
            따라서 2D DP로 풀 수 있으며, dp table은 다음과 같다.
                dp[r][c] = (up 칸까지의 unique path) + (left 칸까지의 unique path)
                         = dp[r - 1][c] + dp[r][c - 1]
            이때, dp table의 첫 번째 row와 column에 있는 칸들은 모두 도달할 수 있는 unique path의 개수가 1이므로 초기화해준다.
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 첫 번째 row & column 초기화
        for r in range(m):
            dp[r][0] = 1
        for c in range(n):
            dp[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]

    def uniquePaths(self, m: int, n: int) -> int:
        """
        [Complexity]
            - TC: O(m * n)
            - SC: O(n) (1D DP로 space optimization)

        [Approach]
            2D DP에서 dp[r][c]를 구할 때 dp[r - 1][c]과 dp[r][c - 1]만 사용하므로,
            rolling array 기법을 이용해 1D DP로 space optimization이 가능하다.
            따라서 길이가 n인 1D dp list를 이용해
                - c(= 1 ~ n - 1)를 순회하며 dp[c] += dp[c - 1]로 업데이트하는 것을 (2D DP에서의 dp[r - 1][c]가 dp[c] 값이므로!)
                - row 개수인 m 번 반복
            하면 된다.
        """

        dp = [0] * n
        dp[0] = 1

        for _ in range(m):
            for c in range(1, n):
                dp[c] += dp[c - 1]

        return dp[n - 1]
