from typing import List
from unittest import TestCase, main


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        return self.solve_sort_stack(intervals)

    """
    LintCode 로그인이 안되어서 hhttps://neetcode.io/problems/meeting-schedule 에서 실행시키고 통과만 확인했습니다.

    Runtime: ? ms (Beats ?%)
    Time Complexity: O(n log n)
        - intervals 정렬에 O(n log n)
        - intervals 조회하며 stack의 마지막 값의 end와 현재 interval의 start를 비교하는데 O(n)
        > O(n log n) + O(n) ~= O(n log n)

    Memory: ? MB (Beats ?%)
    Space Complexity: O(n)
        - intervals 메모리를 그대로 사용하면서 정렬했으므로 O(1)
        - stack의 크기는 최대 intervals와 같아질 수 있으므로 O(n)
    """

    def solve_sort_stack(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        stack: List[Interval] = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue

            if stack[-1].end > interval.start:
                return False
            else:
                stack.append(interval)

        return True


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        intervals = [Interval(0,30), Interval(5,10), Interval(15,20)]
        output = False
        self.assertEqual(Solution().canAttendMeetings(intervals), output)

    def test_2(self):
        intervals = [Interval(5, 8), Interval(9,15)]
        output = False
        self.assertEqual(Solution().canAttendMeetings(intervals), output)

    def test_3(self):
        intervals = [Interval(0, 1), Interval(1, 2)]
        output = False
        self.assertEqual(Solution().canAttendMeetings(intervals), output)


if __name__ == '__main__':
    main()
