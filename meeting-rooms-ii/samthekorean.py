class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pairs = []
        for start, end in intervals:
            pairs += [(start, 1), (end, -1)]
        pairs.sort()

        max_cnt, cnt = 0, 0
        for pair in pairs:
            cnt += pair[1]
            max_cnt = max(cnt, max_cnt)
        return max_cnt
