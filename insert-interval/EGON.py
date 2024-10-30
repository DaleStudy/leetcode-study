from bisect import bisect_left
from typing import List
from unittest import TestCase, main


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return self.solve(intervals, newInterval)

    """
    Runtime: 1 ms (Beats 95.76%)
    Time Complexity: O(n)
    > intervals의 전체를 선형적으로 조회하므로 O(n), 그 외의 append등의 연산들은 O(1)이므로 무시
    
    Memory: 18.70 MB (Beats 99.60%)
    Space Complexity: O(n)
    > result의 크기는 intervals와 newInterval이 하나도 겹치지 않는 경우, 최대 n + 1이므로, O(n + 1) ~= O(n)
    """
    def solve(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        result = []
        new_s, new_e = newInterval
        for interval in intervals:
            s, e = interval
            if e < new_s:
                result.append(interval)
            elif new_e < s:
                if new_s != -1 and new_e != -1:
                    result.append([new_s, new_e])
                    new_s = new_e = -1

                result.append(interval)
            else:
                new_s = min(new_s, s)
                new_e = max(new_e, e)

        if new_s != -1 and new_e != -1:
            result.append([new_s, new_e])

        return result


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        output = [[1,2],[3,10],[12,16]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)

    def test_2(self):
        intervals = [[1,2]]
        newInterval = [3,4]
        output = [[1,2], [3,4]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)

    def test_3(self):
        intervals = [[1,3], [5,6]]
        newInterval = [4,5]
        output = [[1,3], [4,6]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)


if __name__ == '__main__':
    main()
