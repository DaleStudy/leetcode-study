class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPro = 0

        for i in range(1, len(prices)):
            maxPro = max(maxPro, prices[i] - minPrice)
            minPrice = min (minPrice, prices[i])

        return maxPro
        ## TC: O(n) SC: O(1)..?
