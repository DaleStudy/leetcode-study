from typing import List
from unittest import TestCase, main


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.solve_stack(intervals)

    """
    Runtime: 8 ms (Beats 49.77%)
    Time Complexity: 
        - intervals의 길이를 n이라 하면, intervals를  시작 지점을 기준으로 정렬하는데 O(n log n)
        - intervals를 조회하면서 연산하는데, 내부 연산은 모두 O(1)이므로 O(n)
        > O(n log n) + O(n) ~= O(n log n)

    Memory: 19.88 MB (Beats: 99.31%)
    Space Complexity: O(n)
        - intervals는 내부 정렬만 했으므로 추가 메모리 사용 메모리 없음
        - 겹치는 구간이 없는 최악의 경우 merged의 크기는 intervals의 크기와 같아지므로, O(n) upper bound
    """

    def solve_stack(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
                continue

            new_start, new_end = interval
            _, last_end = merged[-1]
            if last_end < new_start:
                merged.append(interval)
            else:
                merged[-1][1] = max(last_end, new_end)

        return merged


class _LeetCodeTestCases(TestCase):

    def test_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        output = [[1, 6], [8, 10], [15, 18]]

        self.assertEqual(Solution().merge(intervals), output)

    def test_2(self):
        intervals = [[1, 4], [4, 5]]
        output = [[1, 5]]

        self.assertEqual(Solution().merge(intervals), output)


if __name__ == '__main__':
    main()
