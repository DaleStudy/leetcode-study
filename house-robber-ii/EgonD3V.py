from collections import deque
from typing import List
from unittest import TestCase, main


class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.solve_dp(nums)

    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(n)
        - 인덱스가 0인 곳을 도둑질한 경우에 대한 dp1에서, 인덱스 2부터 n-2까지 조회하므로 O(n - 3)
            - 각 조회마다 2항 max 연산을 2회씩 하므로 * O(2 * 2)
        - 인덱스가 0인 곳을 도둑질하지 않는 경우에 대한 dp2에서, 인덱스 2부터 n-1까지 조회하므로 O(n - 2)
            - 각 조회마다 2항 max 연산을 2회씩 하므로 * O(2 * 2)
        - 그 외에 정해진 횟수의 max 연산들은 무시, O(C)
        > O(n - 3) * O(2 * 2) + O(n - 4) * O(2 * 2) + O(C) ~= O(n) * O(4) ~= O(n)  

    Memory: 16.59 (Beats 62.16%)
    Space Complexity: O(n)
        - dp1과 dp2가 각각 nums의 길이와 같으므로 O(n * 2)
        > O(n * 2) ~= O(n)
    """
    def solve_dp(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        dp1 = [0] * len(nums)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        max_dp1 = max(dp1[0], dp1[1])
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
            max_dp1 = max(max_dp1, dp1[i])

        dp2 = [0] * len(nums)
        dp2[0], dp2[1] = 0, nums[1]
        max_dp2 = max(dp2[0], dp2[1])
        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
            max_dp2 = max(max_dp2, dp2[i])

        return max(max_dp1, max_dp2)


class _LeetCodeTestCases(TestCase):

    def test_1(self):
        nums = [2, 3, 2]
        output = 3
        self.assertEqual(Solution.rob(Solution(), nums), output)

    def test_2(self):
        nums = [1, 2, 3, 1]
        output = 4
        self.assertEqual(Solution.rob(Solution(), nums), output)


if __name__ == '__main__':
    main()
