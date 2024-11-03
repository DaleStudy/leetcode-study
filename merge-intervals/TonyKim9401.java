// TC: O(n log n)
// It takes n log n to sort array, visit all elements in O(n) time, total O(n log n)
// SC: O(n)
// Needs max O(n) space to save intervals
class Solution {
    public int[][] merge(int[][] intervals) {
        int n = intervals.length;
        if (n == 1) return intervals;

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> output = new ArrayList<>();
        output.add(intervals[0]);

        int[] currentInterval = intervals[0];

        for (int[] interval : intervals) {
            int currentEnd = currentInterval[1];
            int nextStart = interval[0];
            int nextEnd = interval[1];
            if (currentEnd >= nextStart) {
                currentInterval[1] = Math.max(currentEnd, nextEnd);
            } else {
                currentInterval = interval;
                output.add(currentInterval);
            }
        }

        return output.toArray(new int[output.size()][]);
    }
}
