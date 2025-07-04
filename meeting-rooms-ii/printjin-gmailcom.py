class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        s = e = rooms = 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
            else:
                e += 1
            s += 1
        return rooms
