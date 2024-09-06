from typing import List
from unittest import TestCase, main


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.solveWithDP(nums)

    """
    Runtime: 71 ms (Beats 61.13%)
    Time Complexity: O(n)
        - dp 배열 초기화를 위한 nums.copy()에 O(n)
        - range(1, L) 조회하며 조건에 따라 연산에 O(n - 1)
        - range(L) 조회하며 max 계산에 O(n)
        > O(n) + O(n - 1) + O(n) ~= O(n)

    Memory: 17.75 MB (Beats 11.09%)
    Space Complexity: O(n)
        - 크기가 n인 배열 2개 사용했으므로 2 * O(n)
        > O(2n) ~= O(n)
    """
    def solveWithDP(self, nums: List[int]) -> int:
        L = len(nums)
        forward_product, backward_product = nums.copy(), nums.copy()
        for i in range(1, L):
            if forward_product[i - 1] != 0:
                forward_product[i] *= forward_product[i - 1]

            if backward_product[L - i] != 0:
                backward_product[L - i - 1] *= backward_product[L - i]

        result = nums[0]
        for i in range(L):
            result = max(result, forward_product[i], backward_product[i])

        return result


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [2,3,-2,4]
        output = 6
        self.assertEqual(Solution.maxProduct(Solution(), nums), output)

    def test_2(self):
        nums = [-2,0,-1]
        output = 0
        self.assertEqual(Solution.maxProduct(Solution(), nums), output)

    def test_3(self):
        nums = [-2]
        output = -2
        self.assertEqual(Solution.maxProduct(Solution(), nums), output)

    def test_4(self):
        nums = [0,-3,-2,-3,-2,2,-3,0,1,-1]
        output = 72
        self.assertEqual(Solution.maxProduct(Solution(), nums), output)

    def test_5(self):
        nums = [7, -2, -4]
        output = 56
        self.assertEqual(Solution.maxProduct(Solution(), nums), output)


if __name__ == '__main__':
    main()
