class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        rooms_needed, end_pointer = 0, 0

        start_times = sorted([interval[0] for interval in intervals])
        end_times = sorted([interval[1] for interval in intervals])

        for i in range(len(start_times)):
            if start_times[i] >= end_times[end_pointer]:
                end_pointer += 1
            else:
                rooms_needed += 1

        return rooms_needed

        ## TC: O(nlogn), SC: O(n)
