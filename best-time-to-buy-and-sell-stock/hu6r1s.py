class Solution:
    """
    1. 브루트포스
    2중 for문이라서 O(n^2)임.
    prices의 길이가 10^5이므로 10^10이 되면서 시간초과가 발생

    2. 이분탐색으로 가능할까 했지만 DP를 사용해야 하는 문제 같음
    시간복잡도는 O(n)이 나옴
    """
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(price, min_price)
        return max_profit
