# Time Complexity: O(N log N) - sorting takes O(N log N), and merging takes O(N)
# Space Complexity: O(N) - store the merged intervals in a new list.
    
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals by their start values
        intervals.sort(key=lambda x: x[0])

        # this will store our final merged intervals
        merged = [] 
        # start with the first interval
        prev = intervals[0]  
        
        # iterate through the sorted intervals
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:  
                # overlapping intervals → merge them by updating 'end' value
                prev[1] = max(prev[1], interval[1])
            else:
                # no overlap → add 'prev' to the merged list and update 'prev'
                merged.append(prev)
                prev = interval

        merged.append(prev)
        
        return merged
