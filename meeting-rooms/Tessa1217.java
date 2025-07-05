import java.util.Collections;
import java.util.List;

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

    // 시간복잡도: O(n log n) - 정렬, 공간복잡도: O(1)
    public boolean canAttendMeetings(List<Interval> intervals) {
        // Write your code here

        if (intervals == null || intervals.isEmpty()) return true;

        Collections.sort(intervals, (i1, i2) -> i1.start - i2.start);

        Interval previous = intervals.get(0);

        for (int i = 1; i < intervals.size(); i++) {
            Interval current = intervals.get(i);
            if (previous.end > current.start) {
                return false;
            }
            previous = current;
        }

        return true;
    }
}

