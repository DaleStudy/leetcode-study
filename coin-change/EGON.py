from typing import List
from unittest import TestCase, main
from collections import defaultdict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.solve_with_dp(coins, amount)

    # Unbounded Knapsack Problem
    def solve_with_dp(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort()

        if amount < coins[0]:
            return -1

        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for curr_r in range(1, len(coins) + 1):
            coin_index = curr_r - 1
            curr_coin = coins[coin_index]
            if amount < curr_coin:
                continue

            dp[curr_r][curr_coin] += 1
            for curr_amount in range(curr_coin + 1, amount + 1):
                for coin in coins:
                    if 0 < dp[curr_r][curr_amount - coin]:
                        dp[curr_r][curr_amount] = max(dp[curr_r - 1][curr_amount], dp[curr_r][curr_amount - coin] + 1)
                    else:
                        dp[curr_r][curr_amount] = dp[curr_r - 1][curr_amount]

        return dp[-1][-1] if 0 < dp[-1][-1] else -1


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        coins = [1, 2, 5]
        amount = 11
        output = 3
        self.assertEqual(Solution.coinChange(Solution(), coins, amount), output)

    def test_2(self):
        coins = [2]
        amount = 3
        output = -1
        self.assertEqual(Solution.coinChange(Solution(), coins, amount), output)

    def test_3(self):
        coins = [1]
        amount = 0
        output = 0
        self.assertEqual(Solution.coinChange(Solution(), coins, amount), output)

    def test_4(self):
        coins = [1, 2147483647]
        amount = 2
        output = -1
        self.assertEqual(Solution.coinChange(Solution(), coins, amount), output)


if __name__ == '__main__':
    main()
