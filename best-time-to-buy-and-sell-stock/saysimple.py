"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
# - time complexity : O(n)
# - space complexity : O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        now = prices[0]
        diff = [0] * len(prices)

        for i, v in enumerate(prices[1:]):
            if now > v:
                now = v
            else:
                diff[i+1] = v - now

        return max(diff)
