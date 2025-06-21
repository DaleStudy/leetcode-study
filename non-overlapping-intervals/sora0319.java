public class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int count = 0;

        int prv_end = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            if (prv_end > start) {
                count++;
                prv_end = Math.min(end, prv_end);
            } else {
                prv_end = end;
            }
        }
        return count;
    }
}

