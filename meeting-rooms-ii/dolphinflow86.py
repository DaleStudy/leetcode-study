# N is the number of meeting intervals.
# TC: O(N log N) - sorting intervals by start time and maintaining a min-heap
# SC: O(N) - heap stores at most N end times in the worst case

import heapq
from typing import Any, List


class Solution:

    def minMeetingRooms(self, intervals: List[Any]) -> int:
        if not intervals:
            return 0

        # Support both List[List[int]] and List[Interval]
        def get_interval(item):
            if hasattr(item, "start") and hasattr(item, "end"):
                return item.start, item.end
            return item[0], item[1]

        normalized = [get_interval(interval) for interval in intervals]
        normalized.sort(key=lambda x: x[0])

        min_heap = []
        for start, end in normalized:
            if min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)

        return len(min_heap)

    min_meeting_rooms = minMeetingRooms
