# 문제: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def solution(prices):
    profit, buy = 0, prices[0]
    for price in prices:
        diff = price - buy
        buy = min(price, buy)
        profit = max(profit, diff)
    return profit


# 시간복잡도: O(n)
# 공간복잡도: O(1)


answer_1 = solution([7, 1, 5, 3, 6, 4])
answer_2 = solution([7, 6, 4, 3, 1])

print(answer_1 == 5)
print(answer_2 == 0)
