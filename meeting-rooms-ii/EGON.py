from typing import List
from unittest import TestCase, main


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        return self.solve_two_pointer(intervals)

    """
    LintCode 로그인이 안되어서 https://neetcode.io/problems/meeting-schedule-ii 에서 실행시키고 통과만 확인했습니다.

    Runtime: ? ms (Beats ?%)
    Time Complexity: O(n log n)
        - intervals의 길이를 n이라 하면, starts를 정렬하는데 O(n log n)
        - ends를 정렬하는데 O(n log n)
        - intervals를 인덱스를 이용해 전체 조회하는데 O(n)
        > O(n log n) * 2 + O(n) ~= O(n log n)

    Memory: ? MB (Beats ?%)
    Space Complexity: O(n)
        - starts와 ends의 크기는 intervals와 같으므로 O(n)
        - 포인터로 index를 사용했으므로 O(1)
        > O(n) + O(1) ~= O(n)
    """
    def solve_two_pointer(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts, ends = sorted([i.start for i in intervals]), sorted([i.end for i in intervals])
        start_idx, end_idx = 0, 0
        schedule_count = 0
        while start_idx < len(intervals):
            if starts[start_idx] < ends[end_idx]:
                schedule_count += 1
                start_idx += 1
            else:
                end_idx += 1
                start_idx += 1

        return schedule_count


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        intervals = [Interval(0,40), Interval(5,10), Interval(15,20)]
        output = 2
        self.assertEqual(Solution().minMeetingRooms(intervals), output)

    def test_2(self):
        intervals = [Interval(4, 9)]
        output = 1
        self.assertEqual(Solution().minMeetingRooms(intervals), output)

    def test_3(self):
        intervals = [
            Interval(1, 5),
            Interval(2, 6),
            Interval(3, 7),
            Interval(4, 8),
            Interval(5, 9),
        ]
        output = 4
        self.assertEqual(Solution().minMeetingRooms(intervals), output)


if __name__ == '__main__':
    main()
