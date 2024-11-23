from unittest import TestCase, main


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.solve_manacher_algorithm(s)

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

    """
    Runtime: 36 ms (Beats 98.09%)
    Time Complexity: O(n ^ 2)
        - s의 길이를 n이라 하면, s의 길이 - 1 만큼 조회하는데 O(n - 1)
        - 각 문자마다 two_pointer 2회 호출하는데, 각 호출마다 최대 s의 길이만큼 반복하므로, * 2 * O(n), upper bound
        > O(n - 1) * (2 * O(n)) ~= O(n ^ 2)

    Memory: 16.85 MB (Beats 24.42%)
    Space Complexity: O(1)
        > 모든 변수는 result를 제외하고 인덱스를 위한 정수 변수만 사용하므로 O(1)
    """
    def solve_two_pointer(self, s: str) -> str:

        if len(s) < 2 or s == s[::-1]:
            return s

        def two_pointer(left: int, right: int) -> (int, int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s) - 1):
            first_left, first_right = two_pointer(i, i)
            second_left, second_right = two_pointer(i, i + 1)

            if first_right - first_left > end - start:
                start, end = first_left, first_right
            if second_right - second_left > end - start:
                start, end = second_left, second_right

        return s[start: end + 1]

    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def solve_manacher_algorithm(self, s: str) -> str:
        SEPARATOR = '@'
        # Step 1: Transform the string
        t = SEPARATOR + SEPARATOR.join(s) + SEPARATOR
        n = len(t)
        p = [0] * n
        center = right = 0  # Center and right boundary
        max_length = 0
        max_center = 0

        # Step 2: Calculate palindrome radius for each character
        for c in range(n):
            # Use previously calculated information (symmetry)
            if c < right:
                p[c] = min(p[2 * center - c], right - c)

            # Try to expand around i
            while (0 <= c - p[c] - 1 and c + p[c] + 1 < n) and (t[c - p[c] - 1] == t[c + p[c] + 1]):
                p[c] += 1

            # Update center and right boundary if expanded beyond current right
            if c + p[c] > right:
                center = c
                right = c + p[c]

            # Update max palindrome length and center
            if p[c] > max_length:
                max_length = p[c]
                max_center = c

        # Step 3: Extract the original string's palindrome
        start = (max_center - max_length) // 2
        return s[start:start + max_length]


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
