from typing import List
from unittest import TestCase, main


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.solveWithTwoPointer(height)

    """
    Runtime: 527 ms (Beats 47.12%)
    Time Complexity: O(n)
        - 투 포인터의 총합 조회 범위가 height의 길이와 같으므로 O(n)
        - area 갱신을 위한 계산에서 항이 2개인 max와 항이 2개인 min 중첩에 O(2) * O(2)
        > O(n) * O(4) ~= O(n)

    Memory: 29.61 MB (Beats 38.93%)
    Space Complexity: O(1)
        > 정수형 변수들만 사용했으므로 O(1)
    """
    def solveWithTwoPointer(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            area = max(area, (right - left) * min(height[right], height[left]))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return area


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        self.assertEqual(Solution.maxArea(Solution(), height), output)

    def test_2(self):
        height = [1, 1]
        output = 1
        self.assertEqual(Solution.maxArea(Solution(), height), output)


if __name__ == '__main__':
    main()
