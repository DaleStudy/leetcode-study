# TC: O(N), SC: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit

# TS 풀이
# 배열 요소(숫자값)을 직접 순회하려면 for ... of 사용 혹은 forEach
# for ... in -> 인덱스를 가져옴

# function maxProfit(prices: number[]): number {
#     let max_profit: number = 0;
#     let min_price: number = prices[0];

#     for (let price of prices) {
#         max_profit = Math.max(max_profit, price - min_price);
#         min_price = Math.min(min_price, price);
#     }
#     return max_profit;
# };
