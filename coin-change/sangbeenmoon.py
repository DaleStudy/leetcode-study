# dp[i] = min(dp[i - c0], dp[i - c1], ... , dp[i - cn]) + 1

# TC : O(amount * len(coins))
# SC : O(amount)

class Solution:
    dp = []
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [-2] * (amount + 10)  # 아직 방문하지 않음 -> -2
        
        return self.go(amount, coins)
        
        
    def go(self, x: int, coins: List[int]) -> int:
        if x == 0:
            return 0

        if self.dp[x] != -2:
            return self.dp[x]
        
        mm = 100000

        for coin in coins:
            if x - coin >= 0:
                sub = self.go(x - coin, coins)
                if (sub == -1): # 불가능 -> -1
                    continue
                mm = min(mm, sub + 1)
        
        self.dp[x] = mm if mm != 100000 else -1 # memoization
            
        return self.dp[x]
