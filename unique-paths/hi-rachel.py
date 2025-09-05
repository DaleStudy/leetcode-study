"""
https://leetcode.com/problems/unique-paths/description/

아래로 이동 혹은 (1, 0)
오른쪽 이동만 가능 (0, 1)

m => rows, n = cols
로봇이 (0, 0)에서 (m-1, n-1)에 도착 가능한 unique paths 개수를 반환

풀이 시간: 16분
처음에 어떻게 풀어야 할 줄 몰랐지만, 그림을 그려보며 누적 규칙을 찾음 (위, 왼쪽 값 더해나가기)
paths[i][j] = paths[i-1][j] + paths[i][j-1]

TC: O(m * n)
SC: O(m * n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * n for _ in range(m)]
        paths[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
                else:
                    paths[i][j] = 1

        return paths[m - 1][n - 1]


"""
공간 복잡도 최적화 풀이 - 복습 필요
dp[i][j] = dp[i-1][j] + dp[i][j-1]
=> dp[j] = dp[j] + dp[j-1]

TC: O(m * n)
SC: O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 첫 행은 모두 1로 초기화
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[-1]
