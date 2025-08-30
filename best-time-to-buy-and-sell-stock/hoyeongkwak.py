'''
time complexity : O(n)
space complexity : O(2n)

Algorithm : dp
주식 보유하는 경우:
- 이전에 이미 보유 : hold[i - 1]
- i번째 날 새로 사는 경우 : -prices[i]

주식을 팔았을 떄:
- 이전에 이미 팜 : sold[i - 1]
- i번째 날 파는 경우 : hold[i-1] + prices[i]
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        hold = [0] * n
        sold = [0] * n

        hold[0] = -prices[0]
        sold[0] = 0

        for i in range(1, n):
            hold[i] = max(hold[i - 1], -prices[i])
            sold[i] = max(sold[i - 1], hold[i - 1] + prices[i])
        return sold[n - 1]
