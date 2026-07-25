# 1) Use top-down memoization, recursively calculate the minimum coins required for each remaining amount and cache the results to prune duplicated branches.
# TC: O(K^M) where K is the number of coins, where M is the amount. We can recurse down at most M depth
# SC: O(K + M)
class Solution:
    def dfs(self, coins: List[int], memo:Dict[int, int], remain: int):
        if remain == 0: return 0
        if remain < 0: return float('inf')
        if remain in memo: return memo[remain]

        min_result = float('inf')
        for coin in coins:
            min_result = min(min_result, self.dfs(coins, memo, remain - coin))

        memo[remain] = min_result if min_result == float('inf') else min_result + 1
        return memo[remain]

    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.dfs(coins, {}, amount)
        return result if result != float('inf') else -1
