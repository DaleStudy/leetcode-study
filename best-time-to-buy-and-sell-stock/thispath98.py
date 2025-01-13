class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        answer = 0
        for i in range(1, len(prices)):
            if minimum > prices[i]:
                minimum = prices[i]
            else:
                diff = prices[i] - minimum
                if answer < diff:
                    answer = diff
        return answer
