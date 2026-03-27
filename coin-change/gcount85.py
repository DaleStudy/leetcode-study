"""
# Intuition
dp[n]은 n원을 만드는데 필요한 최소 동전 개수
e.g. n = 11일 때, 11원을 만들기 위한 최소 동전 개수는 11에서 coins의 원소를 뺀 dp 값 + 1이다.

# Complexity
- Time complexity: O(amount * coins.length)인데, coins 배열 길이가 상수라서 무시 => O(amount)

- Space complexity: dp 배열 생성으로 O(amount)
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        INF = float("inf")
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            if dp[i] == INF:
                continue
            for c in coins:
                if i + c > amount:
                    break
                dp[i + c] = min(dp[i + c], dp[i] + 1)
        return dp[-1] if dp[-1] != INF else -1
