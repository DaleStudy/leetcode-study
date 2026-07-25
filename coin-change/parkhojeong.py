class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [1 if x in coins else 0 for x in range(amount + 1)]
        MAX_VALUE = sys.maxsize

        for i in range(1, amount + 1):
            if dp[i] != 0:
                continue

            dp[i] = MAX_VALUE
            for coin in coins:
                if i - coin > 0 and dp[i - coin] > 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        if dp[amount] == MAX_VALUE:
            return -1

        return dp[amount]
