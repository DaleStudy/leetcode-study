# 문제내용
# 한번에 1칸 또는 2칸을 오를수있음 정확히 n칸에 도달할수있는 방법수를 구하라
# 계단 문제 = 피보나치 수열
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1칸 또는 0칸 계단은 방법이 1가지뿐
        if n <= 1:
            return 1

        # dp[0] = 1, dp[1] = 1
        prev2, prev1 = 1, 1  # (n-2), (n-1)

        # n=2부터 n까지 반복
        for _ in range(2, n + 1):
            curr = prev1 + prev2  # 현재 계단 방법 수 = 이전 두 계단의 합
            prev2, prev1 = prev1, curr  # 한 칸씩 전진
        return prev1
