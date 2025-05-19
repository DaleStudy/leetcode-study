from typing import List

class Solution:
    """
        - Time Complexity: O(CA), C = len(coins), A = amount
        - Space Complexity: O(A), A = amount
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0   # 0 amount needs 0 coin

        for coin in coins:
            for i in range(coin, amount + 1):
                # dp[i] => not use current coin
                # dp[i - coin] + 1 => use current coin
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1

tc = [
        ([1,2,5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0)
]

for i, (coins, amount, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.coinChange(coins, amount)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
