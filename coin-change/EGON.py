from typing import List
from unittest import TestCase, main
from collections import defaultdict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.solve_with_dfs(coins, amount)

    """
    Runtime: 2039 ms (Beats 5.01%)
    Time Complexity: ?

    Memory: 16.81 MB (Beats 11.09%)
    Space Complexity: ?
    """

    # TIME LIMIT
    def solve_with_dfs(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        result = float('INF')
        stack = []
        for coin in coins:
            stack.append([[coin], coin])
        while stack:
            curr_coins, curr_amount = stack.pop()

            if amount < curr_amount:
                continue

            if curr_amount == amount:
                result = min(result, len(curr_coins))

            for coin in coins:
                stack.append([curr_coins + [coin], curr_amount + coin])

        return -1 if result == float('INF') else result


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


if __name__ == '__main__':
    main()
