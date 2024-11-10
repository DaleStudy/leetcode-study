import java.util.List;

//  Definition of Interval:
class Interval {
    int start, end;
    Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }
}


public class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
    public boolean canAttendMeetings(List<Interval> intervals) {
        // 풀이: 정렬 후 양옆을 비교해가며 조건에 맞지 않으면 false 를 반환한다.
        // TC: O(N)
        // SC: O(1)

        var sortedIntervals = intervals.stream().sorted().toList();

        for (int i=0; i<sortedIntervals.size()-1; i++) {
            if (sortedIntervals.get(i).end > sortedIntervals.get(i+1).start) {
                return false;
            }
        }
        return true;
    }
}
