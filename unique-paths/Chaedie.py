"""
1 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0

Solution: 
    1) grid에서 0,0을 제외하곤 도달할 수 있는 방법이 left way + upper way 갯수밖에 없다고 생각했다.
    2) 따라서 grid를 순회하며 grid index의 경계를 넘어가지 않을 경우 left way + upper way 갯수를 더해주었다.
    3) 마지막 grid의 우하단의 값을 return 해주었습니다.
Time: O(mn) (원소의 갯수)
Space: O(mn) (원소의 갯수)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            dp.append([0] * n)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue

                up_value = 0 if i - 1 < 0 or i - 1 >= m else dp[i - 1][j]
                left_value = 0 if j - 1 < 0 or j - 1 >= n else dp[i][j - 1]

                dp[i][j] = up_value + left_value

        return dp[m - 1][n - 1]


"""
* 7주차에 받은 리뷰사항 뒤늦게 반영합니다.
Solution: 
    1) dp를 1로 m*n 배열로 초기화
    2) 순회를 1부터 m, 1부터 n까지로 변경
    3) up_value, left_value 를 Out of bounds 처리 없이 dp 배열로 계산

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
