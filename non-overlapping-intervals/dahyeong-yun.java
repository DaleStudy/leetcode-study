/**
 * TC : O(n log n)
 *   - intervals 배열의 길이 n 을 최초 정렬 하므로 O(n log n)
 *   - 이후 for loop 는 O(n)
 * SC : O(1)
 *   - 별도 유의미한 공간 할당은 없음
 */
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

        int count = 1;
        int beforeEnd = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] >= beforeEnd) {
                count++;
                beforeEnd = intervals[i][1];
            }
        }
        return intervals.length - count;
    }
}
