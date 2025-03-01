# Time Complexity: O(N log N) 
# (1) sorting the intervals takes O(N log N), and 
# (2) iterating through them takes O(N).
# (3) so the overall complexity is O(N log N).
# Space Complexity: O(1) - only use a few extra variables (end and res), so the space usage is constant.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals by their ending time
        intervals.sort(key=lambda x: x[1])  
        
        # track the last non-overlapping interval's end
        end = float('-inf') 
        # count the number of intervals we need to remove
        res = 0  

        for interval in intervals:
            # if it overlaps with the last interval
            if interval[0] < end: 
                # need to remove this one 
                res += 1  
            else:
                # otherwise, update the end to the current interval's end
                end = interval[1] 
        return res
