'''
시간 복잡도: O(n log n)
공간 복잡도: O(1)
'''
import unittest
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        for i in range(len(intervals) - 1):
            if intervals[i + 1].start < intervals[i].end:
                return False
        
        return True

class TestCanAttendMeetings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
        self.assertFalse(self.solution.can_attend_meetings(intervals))
    
    def test_case_2(self):
        intervals = [Interval(5, 8), Interval(9, 15)]
        self.assertTrue(self.solution.can_attend_meetings(intervals))
    
    def test_case_3(self):
        intervals = []
        self.assertTrue(self.solution.can_attend_meetings(intervals))
    
    def test_case_4(self):
        intervals = [Interval(1, 5)]
        self.assertTrue(self.solution.can_attend_meetings(intervals))
    
    def test_case_5(self):
        intervals = [Interval(0, 5), Interval(5, 10), Interval(10, 15)]
        self.assertTrue(self.solution.can_attend_meetings(intervals))
    
    def test_case_6(self):
        intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10)]
        self.assertFalse(self.solution.can_attend_meetings(intervals))

if __name__ == "__main__":
    unittest.main()
