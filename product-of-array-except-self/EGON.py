from typing import List
from unittest import TestCase, main


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.solve_with_no_extra_space(nums)

    """
    Runtime: 290 ms (Beats 12.23%)
    Time Complexity: O(n)
        - 1부터 n까지 순회했으므로 O(n - 1)
        - 1부터 n + 1 까지 순회했으므로 O(n)
        > O(n - 1) + O(n) ~= O(2n) ~= O(n)

    Memory: 25.68 MB (Beats 83.82%)
    Space Complexity: O(n)
        > 크기가 n + 2인 배열 2개를 사용했으므로 O(2 * (n + 2)) ~= O(n)
    """
    def solve_with_prefix_and_suffix(self, nums: List[int]) -> List[int]:
        forward_product = nums[:]
        reverse_product = nums[:]
        for i in range(1, len(nums)):
            forward_product[i] *= forward_product[i - 1]
            reverse_product[len(nums) - i - 1] *= reverse_product[len(nums) - i]
        forward_product = [1] + forward_product + [1]
        reverse_product = [1] + reverse_product + [1]

        return [forward_product[i - 1] * reverse_product[i + 1] for i in range(1, len(nums) + 1)]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [1, 2, 3, 4]
        output = [24, 12, 8, 6]
        self.assertEqual(Solution.productExceptSelf(Solution(), nums), output)

    def test_2(self):
        nums = [-1, 1, 0, -3, 3]
        output = [0, 0, 9, 0, 0]
        self.assertEqual(Solution.productExceptSelf(Solution(), nums), output)


if __name__ == '__main__':
    main()
