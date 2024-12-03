from unittest import TestCase, main
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return self.solve_sliding_window(s, k)

    """
    Runtime: 63 ms (Beats 98.40%)
    Time Complexity: O(n)
        - s에 대해 조회하는데 O(n)
        - dict인 counter를 사용해서 특정 문자의 빈도수 체크, 분기처리, most_common_char 갱신에 O(1)
        - 현재 최장 길이 계산에 int 계산만 사용하므로 O(1)
        > O(n) * O(1) ~= O(n)

    Memory: 16.54 (Beats 76.70%)
    Space Complexity: O(n), upper bound
        - left, right 같은 int 인덱스 변수 할당에 O(1)
        - most_common_char같은 str 변수 할당에 O(1)
        - dict인 counter의 최대 크기는 s의 모든 문자가 다르고 k의 크기가 len(s)인 경우이므로 O(n), upper bound
        > O(n), upper bound
    """
    def solve_sliding_window(self, s: str, k: int) -> int:
        left = right = 0
        counter, most_common_char = defaultdict(int), ""
        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[most_common_char] < counter[s[right]]:
                most_common_char = s[right]

            if (right - left + 1) - counter[most_common_char] > k:
                counter[s[left]] -= 1
                left += 1

        return right - left + 1


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        s = "AABBCC"
        k = 2
        output = 4
        self.assertEqual(Solution.characterReplacement(Solution(), s, k), output)


if __name__ == '__main__':
    main()
