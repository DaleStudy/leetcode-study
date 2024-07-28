// time: O(n * log n)
// space: O(log n)
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));
        int count = 0;
        int min = Integer.MIN_VALUE;

        for (int i=0; i<intervals.length; i++) {
            int x = intervals[i][0];
            int y = intervals[i][1];

            if (x >= min) {
                min = y;
            } else {
                count++;
            }
        }

        return count;
    }
}
