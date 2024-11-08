// TC: O(n log n)
// in order to order the given intervals array
// SC: O(1)
// only constant space necessary
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (o1, o2) -> Integer.compare(o1[1], o2[1]));

        int output = 0;
        int end = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            int[] currentInterval = intervals[i];

            if (currentInterval[0] < end) output += 1;
            else end = currentInterval[1];
        }

        return output;
    }
}
