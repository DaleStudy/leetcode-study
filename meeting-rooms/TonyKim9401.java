// TC: O(n log n)
// list sort
// SC: O(n)
// list sort max use O(n)
public class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        intervals.sort(Comparator.comparingInt(o -> o.start));

        for (int i = 0; i < intervals.size() - 1; i++) {
            Interval preInterval = intervals.get(i);
            Interval postInterval = intervals.get(i+1);

            if (preInterval.end > postInterval.start) return false;
        }
        return true;
    }
}
