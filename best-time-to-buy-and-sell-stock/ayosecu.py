from typing import List
class Solution:
    """
        - Time Complexity: O(n), n = len(prices)
        - Space Complexity: O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

tc = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0)
]

for i, (prices, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.maxProfit(prices)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
