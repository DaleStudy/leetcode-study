from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
         # dp[i]: i 금액을 만들기 위해 필요한 최소 동전 개수
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


# 시간 복잡도:
# - 외부 반복문은 금액(amount)의 범위에 비례하고 -> O(n) (n은 amount)
# - 내부 반복문은 동전의 개수에 비례하므로 -> O(m) (m은 coins의 길이)
# - 총 시간 복잡도: O(n * m)

# 공간 복잡도:
# - dp 배열은 금액(amount)의 크기만큼의 공간을 사용하므로 O(n)
# - 추가 공간 사용은 없으므로 총 공간 복잡도: O(n)
