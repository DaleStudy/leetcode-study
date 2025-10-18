/**
 * Definition of Interval:
 * public class Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
    public boolean canAttendMeetings(List<Interval> intervals) {
        // Write your code here
        intervals.sort((a, b) -> a.start - b.start);    // sort by start time

        int prevEndTime = 0;
        for (Interval meeting : intervals) {
            if (meeting.start < prevEndTime) {
                return false;
            }
            prevEndTime = meeting.end;
        }
        return true;
    }
}