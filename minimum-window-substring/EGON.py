from collections import Counter
from typing import List
from unittest import TestCase, main


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.solve_two_pointer(s, t)

    """
    Runtime: 129 ms (Beats 50.44%)
    Time Complexity: O(S)
        - 문자열 s를 enumerate로 순회하는데 O(S)
        - 순회 후 left를 갱신하는 while문에서 left가 0부터 n까지 단조증가하므로 총 조회는 O(S)
        > O(S) + O(S) ~= O(S)

    Memory: 17.32 MB (Beats 32.52%)
    Space Complexity: O(S)
        - counter 변수의 초기 크기는 O(T)
            - 반복문을 조회하며 counter 갱신, 최악의 경우 s의 모든 문자가 다르고 s == t인 경우 이므로 O(S), upper bound
        > O(S)
    """
    def solve_two_pointer(self, s: str, t: str) -> str:
        counter = Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, char in enumerate(s, start=1):
            missing -= counter[char] > 0
            counter[char] -= 1

            if missing == 0:
                while left < right and counter[s[left]] < 0:
                    counter[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right

                counter[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        output = "BANC"
        self.assertEqual(Solution.minWindow(Solution(), s, t), output)

    def test_2(self):
        s = "a"
        t = "a"
        output = "a"
        self.assertEqual(Solution.minWindow(Solution(), s, t), output)

    def test_3(self):
        s = "a"
        t = "aa"
        output = ""
        self.assertEqual(Solution.minWindow(Solution(), s, t), output)


if __name__ == '__main__':
    main()
