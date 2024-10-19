from typing import List
from unittest import TestCase, main


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.solve_dp(nums)

    """
    Runtime: 5585 ms (Beats 5.91%)
    Time Complexity: O(n * m)
        - dp 배열 생성에 nums의 길이 n 만큼 조회하는데 O(n)
        - 생성한 dp 배열을 조회하는데 O(n)
            - dp[i]에서 점프하는 범위에 의해 * O(2 * m)
        > O(n) + O(n) * O(2 * m) ~= O(n * m)

    Memory: 17.80 MB (Beats 46.08%)
    Space Complexity: O(n)
        > nums의 길이에 비례하는 dp 배열 하나만 사용, O(n)
    """
    def solve_dp(self, nums: List[int]) -> bool:
        dp = [True if i == 0 else False for i in range(len(nums))]
        for i in range(len(nums)):
            if dp[-1] is True:
                return True

            if dp[i] is True:
                for jump in range(-nums[i], nums[i] + 1):
                    if 0 <= i + jump < len(dp):
                        dp[i + jump] = True

        return dp[-1]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [2, 3, 1, 1, 4]
        output = True
        self.assertEqual(Solution.canJump(Solution(), nums), output)


if __name__ == '__main__':
    main()
