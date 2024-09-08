"""TC: O(n), SC: O(1)

아이디어:
- 특정 시점에서 stock을 팔았을때 최고 수익이 나려면 이전 가격 중 가장 낮은 가격에 stock을 사야 한다.
- 모든 시점에 대해 위의 값을 계산하면 전체 기간 중 최고 수익을 구할 수 있다.
    - 이를 위해서 특정 시점 이전까지의 가격 중 가장 싼 가격인 minp값을 관리하고,
    - 각 시점의 가격에서 minp값을 빼서 `현재 최고 수익`을 구한 다음에,
    - `전체 최고 수익`을 max(`현재 최고 수익`, `전체 최고 수익`)으로 업데이트 한다.

SC:
- minp, profit(`전체 최고 수익`) 값을 관리한다. O(1).

TC:
- prices의 가격을 순회하면서 더하기, min, max 연산을 한다. O(n).
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp, profit = prices[0], 0
        for p in prices:
            profit = max(profit, p - (minp := min(minp, p)))
        return profit
