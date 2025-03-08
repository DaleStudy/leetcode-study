 # Time Complexity: O(N) - iterate through the intervals once.
# Space Complexity: O(N) - store the merged intervals in a new list.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        start, end = newInterval

        for interval in intervals:
            if interval[1] < start:
                # no overlap, and the current interval ends before newInterval starts
                output.append(interval)
            elif interval[0] > end:
                # no overlap, and the current interval starts after newInterval ends
                output.append([start, end])  # insert merged interval before appending the remaining ones
                output.extend(intervals[intervals.index(interval):])  # append remaining intervals
                return output
            else:
                # overlapping case: merge intervals
                start = min(start, interval[0])
                end = max(end, interval[1])

        # add the merged interval at the end if it wasn't added earlier
        output.append([start, end])

        return output
