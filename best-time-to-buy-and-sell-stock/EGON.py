from typing import List
from unittest import TestCase, main


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.solveWithStack(prices)

    """
    Runtime: 749 ms (Beats 46.22%)
    Time Complexity: O(n)
        - prices의 길이 n 만큼 조회에 O(n)
        - 조회하며 수행하는 연산들은 .pop, .append, 고정된 크기에 대한 max 이므로 O(1)
        > O(n) * O(1) ~= O(n) 
        
    Memory: 27.33 MB (Beats 91.14%)
    Space Complexity: O(1)
        - 크기가 1로 유지되는 stack: List[int] 사용
        - max_profit: int 사용
        > O(1)
    """
    def solveWithStack(self, prices: List[int]) -> int:
        max_profit = 0
        stack = []
        for price in prices:
            if not stack:
                stack.append(price)
                continue

            min_price = stack.pop()
            if min_price < price:
                max_profit = max(price - min_price, max_profit)
                stack.append(min_price)
            elif min_price > price:
                stack.append(price)
            else:
                stack.append(min_price)

        return max_profit


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        prices = [7,1,5,3,6,4]
        output = 5
        self.assertEqual(Solution.maxProfit(Solution(), prices), output)

    def test_2(self):
        prices = [7,6,4,3,1]
        output = 0
        self.assertEqual(Solution.maxProfit(Solution(), prices), output)


if __name__ == '__main__':
    main()
