class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        주식 가격 목록에서 최대 이익을 계산하는 함수.

        시간 복잡도: O(N)
        공간 복잡도: O(1)

        Args:
            prices (list[int]): 주식 가격 목록

        Returns:
            int: 최대 이익
        """
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit
