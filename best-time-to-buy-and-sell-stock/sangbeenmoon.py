# TC : O(n)
# SC : O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        mm = 10001

        for price in prices:
            mm = min(mm, price)
            answer = max(answer, price - mm)
        
        return answer
