from unittest import TestCase, main


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solveWithDP(n)

    """
    Runtime: 30 ms (Beats 83.62%)
    Time Complexity: O(n)
        > 3에서 n + 1 까지 range를 조회하였으므로 O((n + 1) - 3) ~= O(n)

    Memory: 16.39 MB (Beats 90.15%)
    Space Complexity: O(n)
        > 크기가 n + 1인 dp를 선언하여 사용했으므로 O(n + 1) ~= O(n)
    """
    def solveWithDP(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 2
        for stair in range(3, n + 1):
            dp[stair] = dp[stair - 1] + dp[stair - 2]

        return dp[n]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        n = 2
        output = 2
        self.assertEqual(Solution.climbStairs(Solution(), n), output)

    def test_2(self):
        n = 3
        output = 3
        self.assertEqual(Solution.climbStairs(Solution(), n), output)

    def test_3(self):
        n = 1
        output = 1
        self.assertEqual(Solution.climbStairs(Solution(), n), output)


if __name__ == '__main__':
    main()
