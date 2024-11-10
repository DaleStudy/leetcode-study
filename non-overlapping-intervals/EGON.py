from typing import List
from unittest import TestCase, main


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return self.solve_stack(intervals)

    """
    LintCode 로그인이 안되어서 hhttps://neetcode.io/problems/meeting-schedule 에서 실행시키고 통과만 확인했습니다.

    Runtime: 66 ms (Beats 85.10%)
    Time Complexity: O(n log n)
        - intervals를 정렬하는데 O(n log n)
        - intervals를 조회하며 result stack을 갱신하는데 O(n)
            - 2항에 대한 or 연산 및 append 메서드만 쓰므로 * O(1)
        > O(n log n) + O(n) ~= O(n log n)
    Memory: 50.98 MB (Beats 74.30%)
    Space Complexity: O(n)
        - intervals 정렬도 기존 intervals를 사용하므로 O(1)
        - result의 크기가 최대 interval과 같아질 수 있으므로 O(n)
        > O(1) + O(n) ~= O(n)
    """
    def solve_stack(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        result = []
        for interval in intervals:
            if not result or interval[0] >= result[-1][1]:
                result.append(interval)

        return len(intervals) - len(result)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        intervals = [[1,2],[2,3],[3,4],[1,3]]
        output = 1
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), output)


if __name__ == '__main__':
    main()
