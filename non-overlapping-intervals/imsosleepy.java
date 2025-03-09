// 정렬을 하지 않으면 O(N^2)이 확정인 문제
// 정렬을 해서 O(NlogN)으로 해결
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;

        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

        int count = 0;
        int prevEnd = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < prevEnd) { 
                count++;
            } else {
                prevEnd = intervals[i][1];
            }
        }
        return count;
    }
}

