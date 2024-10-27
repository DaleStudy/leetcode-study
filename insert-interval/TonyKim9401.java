// TC: O(n)
// must retrieve all elements
// SC: O(n)
// need the same size of memory space in the worst case
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> output = new ArrayList<>();

        int i = 0;
        int n = intervals.length;

        while (i < n && intervals[i][1] < newInterval[0]) {
            output.add(intervals[i]);
            i += 1;
        }

        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i += 1;
        }

        output.add(newInterval);

        while (i < n) {
            output.add(intervals[i]);
            i += 1;
        }

        return output.toArray(new int[output.size()][]);
    }
}
