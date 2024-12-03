from typing import List
from unittest import TestCase, main


class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.solve_dp(nums)

    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(n)
        - nums 배열을 조회하며 dp 배열을 갱신하므로 O(n)
            - 2항에 대한 max 연산을 사용하므로 * O(2)
        > O(2 * n) ~= O(n)

    Memory: 16.62 MB (Beats 24.05%)
    Space Complexity: O(n)
        > 길이가 n인 dp 배열을 사용하므로 O(n)
    """

    def solve_dp(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [2,1,1,2]
        output = 4
        self.assertEqual(Solution().rob(nums), output)


if __name__ == '__main__':
    main()
