from typing import List
from unittest import TestCase, main


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.solveWithDP(coins, amount)

    # Unbounded Knapsack Problem
    """
    Runtime: 801 ms (Beats 48.54%)
    Time Complexity: O(n)
        - coins 길이를 c, amount의 크기를 a라고 하면
        - coins를 정렬하는데 O(log c)
        - dp 배열 조회에 O((n + 1) * c)
        > c의 최대 크기는 12라서 무시가능하므로 O((n + 1) * c) ~= O(n * c) ~= O(n) 

    Memory: 16.94 MB (Beats 50.74%)
    Space Complexity: O(n)
        > 크기가 n + 1인 dp를 선언하여 사용했으므로 O(n + 1) ~= O(n)
    """
    def solveWithDP(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort()

        if amount < coins[0]:
            return -1

        dp = [float('inf')] * (amount + 1)

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for curr_amount in range(amount + 1):
            for coin in coins:
                if 0 <= curr_amount - coin:
                    dp[curr_amount] = min(
                        dp[curr_amount],
                        dp[curr_amount - coin] + 1
                    )

        return dp[-1] if dp[-1] != float('inf') else -1


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
        output = 2
        self.assertEqual(Solution.coinChange(Solution(), coins, amount), output)


if __name__ == '__main__':
    main()
