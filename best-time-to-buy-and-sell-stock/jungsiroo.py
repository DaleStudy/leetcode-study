class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        가장 수익을 많이 얻을 수 있도록 저점에 매수, 고점에 매도
        매수와 매도는 서로 다른 날
   		
		min_price를 빼가면서 price 업데이트

		Time Complexity : O(n)
		Space Complexity : O(1)
        """

        min_price = max(prices)
        days = len(prices)
    
        for day in range(days):
			min_price = min(prices[day], min_price)
            prices[day] -= min_price
    
        return max(prices)
    

        
