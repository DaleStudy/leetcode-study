"""
Time Complexity: O(n)
Space Complexity: O(1)

- Single Pass approach
- Use a variable to store the least price
- Use a variable to store the maximum profit
- Update the maximum profit whenever the current price is greater than the least price
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        least = prices[0]
        ans = 0

        for i in range(1, N):
            ans = max(ans, prices[i] - least)
            least = min(least, prices[i])

        return ans
