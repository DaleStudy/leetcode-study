# 시간복잡도: O(N)
# 공간복잡도: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        answer = 0
        cur = float(inf)
        for price in prices:
            if cur < price:
                answer = max(answer, price - cur)

            if price < cur:
                cur = price

        return answer
