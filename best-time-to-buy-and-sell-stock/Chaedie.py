"""
Solution: 1) 2중 포문을 돌면서 max값을 구한다.
Time: O(n^2)
Space: O(1)

Time Limit Exceeded

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for l in range(len(prices) - 1):
            for r in range(l + 1, len(prices)):
                result = max(result, prices[r] - prices[l])

        return result


"""
Solution: 
    1) prices를 순회하면서 max_profit 을 찾는다. 
    2) profit 은 current price - min_profit로 구한다.
Time: O(n)
Space: O(1)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
            min_price = min(prices[i], min_price)
        return max_profit
