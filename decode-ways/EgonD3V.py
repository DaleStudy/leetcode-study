from typing import List
from unittest import TestCase, main


class Solution:
    def numDecodings(self, s: str) -> int:
        return self.solve_1(s)

    """
    Runtime: 32 ms (Beats 80.36%)
    Time Complexity: O(n)
    Space Complexity: O(n)
    Memory: 16.59 MB (Beats 51.72%)
    """
    def solve_1(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 0 if int(s) == 0 else 1

        if len(s) == 2:
            last_one_digit, last_two_digits = int(s[1]), int(s)
            if last_one_digit == 0:
                return 1 if 10 <= last_two_digits <= 26 else 0
            else:
                if 0 <= last_two_digits < 10:
                    return 0
                elif 10 <= last_two_digits <= 26:
                    return 2
                else:
                    return 1

        dp = [0] * (len(s) + 1)
        dp[0], dp[1], dp[2] = self.solve_1(s[:0]), self.solve_1(s[:1]), self.solve_1(s[:2])
        for i in range(3, len(s) + 1):
            last_one_digit, last_two_digits = int(s[i - 1]), int(s[i - 2: i])
            last_two_digits = int(s[i - 2: i])
            if last_one_digit == 0:
                dp[i] += dp[i - 2] if 10 <= last_two_digits <= 26 else 0
            else:
                dp[i] += dp[i - 1] + (dp[i - 2] if 10 <= last_two_digits <= 26 else 0)

        return dp[-1]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        s = "226"
        output = 3
        self.assertEqual(Solution.numDecodings(Solution(), s), output)

    def test_2(self):
        s = "2101"
        output = 1
        self.assertEqual(Solution.numDecodings(Solution(), s), output)

    def test_3(self):
        s = "06"
        output = 0
        self.assertEqual(Solution.numDecodings(Solution(), s), output)


if __name__ == '__main__':
    main()
