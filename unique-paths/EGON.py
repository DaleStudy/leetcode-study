from unittest import TestCase, main


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve_dp(m, n)

    """
    Runtime: 33 ms (Beats 73.78%)
    Time Complexity: O(m * n)
        - m * n 크기의 2차원 배열 dp 생성에 O(m * n)
        - range(1, m) * range(1, n) 중첩 조회에 O((m - 1) * (n - 1))
        - result로 dp[-1][-1] 조회에 O(1)
        > O(m * n) + O((m - 1) * (n - 1)) + O(1) ~= O(m * n) + O(m * n) ~= O(m * n)

    Memory: 16.44 (Beats 77.15%)
    Space Complexity: O(m * n)
        > m * n 크기의 2차원 배열 dp 사용에 O(m * n)
    """
    def solve_dp(self, m: int, n: int) -> int:
        dp = [[1 if r == 0 or c == 0 else 0 for c in range(n)] for r in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        m = 3
        n = 7
        output = 28
        self.assertEqual(Solution.uniquePaths(Solution(), m, n), output)


if __name__ == '__main__':
    main()
