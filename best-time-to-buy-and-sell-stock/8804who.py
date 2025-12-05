class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        min_price = prices[0]
        for price in prices:
            if min_price>price:
                min_price=price
            
            if answer<price-min_price:
                answer=price-min_price
        return answer
    

