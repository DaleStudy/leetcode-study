"""
Constraints:
1. 1 <= coins.length <= 12
2. 1 <= coins[i] <= 2^31 - 1
3. 0 <= amount <= 10^4

Time Complexity: O(N*M) 
- N은 amount
- M은 동전의 개수 (coins.length)

Space Complexity: O(N) 
- N은 amount

To Do:
- DP 문제 복습하기
- Bottom-up과 Top-down 방식의 차이점 이해하기
- 그리디와 DP의 차이점 복습하기
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize // 2] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount] if dp[amount] != sys.maxsize // 2 else -1
