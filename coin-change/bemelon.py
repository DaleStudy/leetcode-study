class Solution:
    # Space complexity: O(n)
    # Time complexity: O(n * m)
    #  - n: amount
    #  - m: len(coins)
    def coinChange(self, coins: list[int], amount: int) -> int:
        INIT_VALUE = 999999999
        dp = [INIT_VALUE] * (amount + 1) 
        dp[0] = 0

        for x in range(1, amount + 1):
            for coin in coins: 
                if x - coin >= 0:
                    dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != INIT_VALUE else -1
