# O(C*A) times, O(A) spaces
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       dp = [0] + [amount + 1] * amount

       for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin]+1)

       return dp[amount] if dp[amount] < amount + 1 else -1
