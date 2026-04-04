class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # When length is 1, no profit possible
        if len(prices) == 1:
            return 0

        buy = 10 ** 5
        profit = 0

        # Iterate through prices
        # for i, price in enumerate(prices):
        #     if price < buy:
        #         buy = price
        #
        #         for j in range(i + 1, len(prices)):
        #             if prices[j] <= buy:
        #                 continue
        #
        #             if prices[j] - buy > profit:
        #                 profit = prices[j] - buy
        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy

        return profit

# Time Complexity: O(n)
# Space Complexity: O(1)
