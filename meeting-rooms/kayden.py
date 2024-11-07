class Solution:
    # 시간복잡도: O(NlogN)
    # 공간복잡도: O(1)
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort()

        prev = 0
        for start, end in intervals:
            if end < prev:
                return False

            prev = end

        return True
