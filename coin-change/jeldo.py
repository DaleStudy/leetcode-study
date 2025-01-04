class Solution:
    # O(n*m), n=len(coins), m=amount
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != amount+1 else -1
