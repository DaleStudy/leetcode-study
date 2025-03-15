 # Time Complexity: O(n log n) -> sorting takes O(n log n), and heap operations take O(log n) per interval.
 # Space Complexity: O(n) -> in the worst case, store all meetings in the heap.

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:        
        if not intervals:
            return 0
        
        # sort meetings by start time.
        intervals.sort() 
        
        # heap to keep track of meeting end times.
        min_heap = [] 
        
        for start, end in intervals:
            if min_heap and min_heap[0] <= start:
                # remove the meeting that has ended.
                heapq.heappop(min_heap) 
            # add the current meeting's end time.
            heapq.heappush(min_heap, end) 
        
        return len(min_heap) 
