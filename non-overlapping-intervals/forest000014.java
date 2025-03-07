/*
# Time Complexity: O(nlogn)
  - 정렬 : O(nlogn)
  - for-loop : O(n)
# Space Complexity: O(1)
*/
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

        int cnt = 0;
        int prev_end = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            if (prev_end > intervals[i][0]) {
                cnt++;
            } else {
                prev_end = intervals[i][1];
            }
        }

        return cnt;
    }
}
