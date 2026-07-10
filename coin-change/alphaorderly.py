"""
Time Complexity: O(n * amount)
Space Complexity: O(n * amount)

- DP / Top-Down approach
- Use a cache to store the results of the subproblems
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        LARGE = 10 ** 5

        @cache
        def dp(coin: int, left: int) -> int:
            if left == 0:
                return 0

            if left < 0:
                return LARGE

            if coin >= len(coins):
                return LARGE

            a = dp(coin, left - coins[coin]) + 1
            b = dp(coin + 1, left)

            return min(a, b)

        ans = dp(0, amount)

        return ans if ans != LARGE else -1

"""
Time Complexity: O(n * amount)
Space Complexity: O(n * amount)

- DP / Bottom-Up approach
- Use a 2D array to store the results of the subproblems
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(N)]

        for c in range(N):
            dp[c][0] = 0

            if c > 0:
                for a in range(amount + 1):
                    dp[c][a] = dp[c - 1][a]

            for a in range(coins[c], amount + 1):
                dp[c][a] = min(dp[c][a], dp[c][a - coins[c]] + 1)

        ans = dp[-1][-1]

        return ans if ans != float('inf') else -1

"""
Time Complexity: O(n * amount)
Space Complexity: O(amount)

- DP / Bottom-Up approach [Space Optimized]
- Use a 1D array to store the results of the subproblems
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for c in range(N):
            for a in range(coins[c], amount + 1):
                dp[a] = min(dp[a], dp[a - coins[c]] + 1)

        ans = dp[-1]

        return ans if ans != float('inf') else -1
