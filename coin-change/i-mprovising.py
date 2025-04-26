"""
Time complexity O(len(coins) * amount)
Space complexity O(amount)

Dynamic programming
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        
        if amount == 0 :
            return 0

        dp = [0] + [-1 for _ in range(amount)]

        for i in range(coins[0], amount+1):
            tmp = []
            for x in coins:
                if i - x >= 0:
                    if dp[i - x] != -1:
                        tmp.append(dp[i - x] + 1)
            if len(tmp) == 0:
                dp[i] = -1
            else:
                dp[i] = min(tmp)

        if dp[-1] == 0:
            return -1
        return dp[-1]
