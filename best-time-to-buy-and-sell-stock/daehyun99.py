class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(prices[r]-prices[l], profit)
            elif prices[l] > prices[r]:
                l = r
            r += 1
        return profit
