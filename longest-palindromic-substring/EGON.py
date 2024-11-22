from unittest import TestCase, main


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.solve_sliding_window(s)

    """
    Runtime: 47 ms (Beats 96.97%)
    Time Complexity: O(n ^ 3)
        - s의 길이를 n이라 하면, s의 길이 - 1 만큼 조회하는데 O(n - 1)
            - 각 문자마다 sliding_window를 2회 호출하는데, 각 호출마다 최대 s의 길이만큼 반복하므로, * 2 * O(n), upper bound
                - 반복 후 s를 slicing하는데 최대 * O(n), upper bound
        > O(n - 1) * (2 * O(n)) * O(n) ~= O(n ^ 3)

    Memory: 16.54 MB (Beats 88.85%)
    Space Complexity: O(n)
        - sliding_window의 결과로 생성되는 문자열의 최대 길이는 n이고, 조회마다 2회 생성되므로 2 * O(n), upper bound
        > 2 * O(n) ~= O(n)
    """
    def solve_sliding_window(self, s: str) -> str:

        def sliding_window(left: int, right: int) -> str:
            while 0 <= left and right < len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1

            return s[left + 1: right - 1]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, sliding_window(i, i + 1), sliding_window(i, i + 2), key=len)

        return result


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        s = "babad"
        output = "bab"
        self.assertEqual(Solution().longestPalindrome(s), output)

    def test_2(self):
        s = "cbbd"
        output = "bb"
        self.assertEqual(Solution().longestPalindrome(s), output)


if __name__ == '__main__':
    main()
