import java.util.Arrays;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {

        // 끝점 기준 정렬
        Arrays.sort(intervals, (o1, o2) -> Integer.compare(o1[1], o2[1]));

        int overlap = 0;

        int end = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            int currentStart = intervals[i][0];
            int currentEnd = intervals[i][1];

            if (currentStart < end) {
                overlap++;
            } else {
                end = currentEnd;
            }

        }

        return overlap;
    }
}

