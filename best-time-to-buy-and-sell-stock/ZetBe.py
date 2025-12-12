'''
문제: 한번의 구매와 판매로 얻을 수 있는 최대 이익을 구하라.
풀이: 주어진 가격 리스트를 순회하면서 최저가와 최고가를 갱신하며 최대 이익을 계산한다.
    최저가는 현재 최저가격보다 낮은 가격이 나오면 갱신하고, 
    최고가는 현재 최고가격보다 높은 가격이 나오면 갱신및 정답인지 비교한다.
시간복잡도: O(n)
공간복잡도: O(1)

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ma, mi = prices[0], prices[0]
        answ = 0
        for i in range(1, len(prices)):
            if mi > prices[i]:
                mi, ma = prices[i], prices[i]
            if ma < prices[i]:
                ma = prices[i]
                answ = max(answ, ma-mi)
        return answ

