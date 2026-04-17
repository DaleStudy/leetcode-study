# 7기 풀이
# 시간 복잡도: O(m * n)
# - m과 n 만큼의 이중 루프를 돌게 됨
# 공간 복잡도: O(m)
# - dp의 결과 값을 저장할 배열의 길이는 m의 길이에 좌우됨
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 이전 열의 값만 필요로 하기 때문에 1차원 배열을 사용하며 in-place 업데이트를 하면 된다.
        dp = [1 for _ in range(m)]

        for _ in range(n - 1):
            for i in range(1, m):
                # 현재 칸 = 위에서 오는 경로 수(갱신 전 dp[i]) + 왼쪽에서 오는 경로 수(dp[i-1])
                dp[i] = dp[i] + dp[i - 1]

        return dp[m - 1]  # 모든 루프를 돌고 나면 도착지 도달 가능 방법수가 저장이 되어 있다.
