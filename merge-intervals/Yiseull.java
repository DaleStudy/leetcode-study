class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (o1, o2) -> o1[0] - o2[0]);

        int index = 0;
        for (int i = 0; i < intervals.length; i++) {
            if (intervals[index][1] < intervals[i][0]) {
                intervals[++index] = intervals[i];
            } else {
                intervals[index][1] = Math.max(intervals[index][1], intervals[i][1]);
            }
        }

        return Arrays.copyOf(intervals, index + 1);
    }
}
