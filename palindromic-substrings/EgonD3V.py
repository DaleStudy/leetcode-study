from unittest import TestCase, main


class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.solve_2(s)

    """
    Runtime: 776 ms (Beats 10.15%)
    Analyze Complexity: O(n ** 3), for * for * slicing
    Memory: 16.43 MB (Beats 73.44%)
    """
    def solve_1(self, s: str) -> int:
        count = 0
        for left in range(len(s)):
            for right in range(left, len(s)):
                substring = s[left: right + 1]
                count += substring == substring[::-1]

        return count

    """
    Runtime: 373 ms (Beats 19.31%)
    Analyze Complexity: O(n ** 2)
    Memory: 25.15 MB (Beats 11.85%)
    """
    def solve_2(self, s: str) -> int:
        dp = [[left == right for left in range(len(s))] for right in range(len(s))]
        count = len(s)

        for i in range(len(s) - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            count += dp[i][i + 1]

        for length in range(3, len(s) + 1):
            for left in range(len(s) - length + 1):
                right = left + length - 1
                dp[left][right] = dp[left + 1][right - 1] and s[left] == s[right]
                count += dp[left][right]

        return count


class _LeetCodeTCs(TestCase):
    def test_1(self):
        s = "abc"
        output = 3
        self.assertEqual(Solution.countSubstrings(Solution(), s), output)

    def test_2(self):
        s = "aaa"
        output = 6
        self.assertEqual(Solution.countSubstrings(Solution(), s), output)


if __name__ == '__main__':
    main()
