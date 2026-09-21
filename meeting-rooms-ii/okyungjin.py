# 253. Meeting Rooms II
# https://www.lintcode.com/problem/919/

"""
문제:
    - 회의 시간 구간 `[start, end)` 목록이 주어진다. (start < end)
    - 모든 회의를 진행하는 데 필요한 최소 회의실 개수를 구한다.
    - 한 회의가 끝나는 시각에 다른 회의가 시작하는 것은 충돌이 아니다.

복잡도:
    n: `intervals`의 길이
    Time: O(n log n)
    Space: O(n)
"""
import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        pq = []
        intervals.sort(key=lambda x: x.start)

        for cur in intervals:
            if pq:
                earliest_end = pq[0]  # 열린 방들 중 가장 빨리 끝나는 시각
                if cur.start >= earliest_end:
                    heapq.heappop(pq)
            heapq.heappush(pq, cur.end)

        return len(pq)

# print(Solution().min_meeting_rooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))  # 2
# print(Solution().min_meeting_rooms([Interval(0, 5), Interval(5, 10), Interval(10, 15)]))  # 1
# print(Solution().min_meeting_rooms([Interval(1, 10), Interval(2, 7), Interval(3, 9), Interval(8, 12)]))  # 3
