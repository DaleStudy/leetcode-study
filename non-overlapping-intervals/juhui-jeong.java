/*
 * 끝나는 시간 오름차순 정렬
 */
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[1], b[1]));
        
        int removeCntResult = 0;
        int end = intervals[0][1];

        for (int i = 1; i< intervals.length; i++) {
            if (intervals[i][0] < end) {
                removeCntResult += 1;
            } else {
                end = intervals[i][1];
            }
        }
        return removeCntResult;
    }
}


/*
처음 풀이
시작 시간 기준 정렬
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });
        
        int removeCntResult = 0;
        int[] cur = intervals[0];

        for (int i = 1; i< intervals.length; i++) {
            int [] next = intervals[i];

            if (cur[1] > next[0]) {
                removeCntResult += 1;
                if (next[1] < cur[1]) {
                    cur = next;
                }
            } else {
                cur = next;
            }
        }
        return removeCntResult;
    }
}
 */
