class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e9] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin>=0:
                    if dp[i-coin]+1<dp[i]:
                        dp[i]=dp[i-coin]+1
        
        return -1 if dp[amount]==1e9 else dp[amount]
    
