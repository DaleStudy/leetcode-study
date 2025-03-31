// 정렬을 하지않으면 O(N^2), 정렬을 하면 최대 O(nlogn) 내에서 해결이 된다.
// 그래서 정렬 후 겹치는지 조회하는 방식 
public static boolean canAttendMeetings(int[][] intervals) {
    if (intervals == null || intervals.length == 0) return true;

    Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

    for (int i = 1; i < intervals.length; i++) {
        if (intervals[i - 1][1] > intervals[i][0]) {
            return false;
        }
    }
    return true;
}
