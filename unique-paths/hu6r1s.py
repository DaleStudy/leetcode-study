class Solution:
    """
    dfs로 풀면 될 것이라고 생각은 했지만 이전 문제와 같은 방식일 줄 알았는데 이러한 방식이 있는 것을 알았음
    """
    # def uniquePaths(self, m: int, n: int) -> int:
    #     def dfs(x, y):
    #         if x == m - 1 and y == n - 1:
    #             return 1
    #         if x >= m or y >= n:
    #             return 0
            
    #         return dfs(x + 1, y) + dfs(x, y + 1)
        
    #     return dfs(0, 0)

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]
