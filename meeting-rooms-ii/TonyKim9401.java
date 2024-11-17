// TC: O(n)
// visit all intervals to compare each of start time
// SC: O(n)
// PQ save all intervals in the worst case
public class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        if (intervals == null || intervals.isEmpty()) return 0;

        intervals.sort((a, b) -> a.start - b.start);

        PriorityQueue<Integer> endTimes = new PriorityQueue<>();
        endTimes.add(intervals.get(0).end);

        for (int i = 1; i < intervals.size(); i++) {
            Interval current = intervals.get(i);
            if (current.start >= endTimes.peek()) endTimes.poll();
            endTimes.add(current.end);
        }

        return endTimes.size();
    }
}
