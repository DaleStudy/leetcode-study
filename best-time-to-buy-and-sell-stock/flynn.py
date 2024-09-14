'''
풀이
- 주어진 배열 prices를 한 번 탐색합니다.

- prices[i]가 이전에 저장한 buy_price보다 낮을 경우,
  maximum profit이 증가할 가능성이 있습니다.
  따라서 buy_price와 sell_price를 prices[i]로 바꿔줍니다.
  
- prices[i]가 이전에 저장한 sell_price보다 높은 경우,
  현재 buy_price로 지금까지 기록한 profit보다 더 높은 이익을 내게 됩니다.
  따라서 sell_price를 prices[i]로 바꿔주고 결과값을 갱신합니다.

Big O
- N: 배열 prices의 크기

- Time complexity: O(N)
  - 배열의 크기 N이 증가함에 따라 실행 시간도 선형적으로 증가합니다.

- Space complexity: O(1)
  - 배열의 크기 N이 증가하여도 사용하는 메모리 공간은 일정합니다.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        res = 0

        buy_price = prices[0]
        sell_price = prices[0]

        for i in range(1, len(prices)):
            curr_price = prices[i]

            if buy_price > curr_price:
                buy_price = curr_price
                sell_price = curr_price
            elif sell_price < curr_price:
                sell_price = curr_price
                res = max(res, sell_price - buy_price)

        return res
