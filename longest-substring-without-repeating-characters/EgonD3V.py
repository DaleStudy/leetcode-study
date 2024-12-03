from unittest import TestCase, main


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.solve_sliding_window(s)

    """
    Runtime: 313 ms (Beats 8.97%)
    Time Complexity:
        - left가 0에서 len(s)까지 조회, right가 left + 1 부터 len(s)까지 조회하므로 O(n * (n + 1) / 2)
            - left가 조회할 때마다, 2항 max 연산하므로 * 2
        > O((n * (n + 1) / 2) * 2) ~= O(n ^ 2)

    Memory: 16.51 (Beats 81.63%)
    Space Complexity: O(n)
        > checker가 최대 s의 길이만큼 커질 수 있으므로 O(n), upper bound
    """
    def solve_two_pointer(self, s: str) -> int:
        if not s:
            return 0

        max_length = 1
        for left in range(len(s)):
            if len(s) - left + 1 < max_length:
                return max_length

            right = left + 1
            checker = set(s[left])
            while right < len(s):
                if s[right] in checker:
                    break

                checker.add(s[right])
                right += 1

            max_length = max(max_length, len(checker))

        return max_length

    """
    Runtime: 58 ms (Beats 46.47%)
    Time Complexity:
        - 중복 검사는 set을 사용하므로 O(1)
        - right가 len(s)까지 조회하므로 O(n)
            - right가 조회한 뒤 2항 max 연산하는데 O(2)
        - left가 최대 right까지 조회하고 right < len(s) 이므로 O(n), upper bound
        > O(n) * O(2) + O(n) ~= O(n)

    Memory: 16.60 (Beats 41.73%)
    Space Complexity: O(n)
        > checker가 최대 s의 길이만큼 커질 수 있으므로 O(n), upper bound
    """
    def solve_sliding_window(self, s: str) -> int:
        max_length = 0
        left = right = 0
        checker = set()
        while left < len(s) and right < len(s):
            while right < len(s) and s[right] not in checker:
                checker.add(s[right])
                right += 1

            max_length = max(max_length, len(checker))

            while left < len(s) and (right < len(s) and s[right] in checker):
                checker.remove(s[left])
                left += 1

        return max_length


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        s = "pwwkew"
        output = 3
        self.assertEqual(Solution.lengthOfLongestSubstring(Solution(), s), output)


if __name__ == '__main__':
    main()
