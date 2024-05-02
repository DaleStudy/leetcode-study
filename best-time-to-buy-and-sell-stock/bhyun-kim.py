"""
Solution

Algorithm:
    1. Iterate through the list in reverse.
    2. Keep track of the maximum value seen so far.
    3. Calculate the profit by subtracting the current value from the maximum value.
    4. Update the profit if it is greater than the current profit.

Time complexity: O(n)
Space complexity: O(1)
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev_max = 0

        for i in reversed(range(len(prices) - 1)):
            prev_max = max(prev_max, prices[i + 1])
            profit = max(profit, prev_max - prices[i])

        return profit


def main():
    test_cases = [[[7, 1, 5, 3, 6, 4], 5], [[7, 6, 4, 3, 1], 0]]
    s = Solution()

    for test_case in test_cases:
        prices_input, expected = test_case
        assert s.maxProfit(prices_input) == expected


if __name__ == "__main__":
    main()
