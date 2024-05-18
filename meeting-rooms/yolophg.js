// Time Complexity: O(n log n)
// Space Complexity: O(1)

class Solution {
    canAttendMeetings(intervals) {
        intervals.sort((a, b) => a.start - b.start);
        
        // check for overlaps.
        for (let i = 1; i < intervals.length; i++) {
          // check if there is an overlap between the current interval and the previous one.
            if (intervals[i].start < intervals[i - 1].end) {
                return false; 
            }
        }

        return true;
    }
}
