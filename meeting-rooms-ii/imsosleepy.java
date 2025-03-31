// 정렬을 이용하면 O(nlogn)으로 풀리는데 다른 아이디어가 안떠오름
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return 0;

        int n = intervals.length;
        int[] startTimes = new int[n];
        int[] endTimes = new int[n];

        for (int i = 0; i < n; i++) {
            startTimes[i] = intervals[i][0];
            endTimes[i] = intervals[i][1];
        }

        Arrays.sort(startTimes);
        Arrays.sort(endTimes);

        int rooms = 0;
        int endPointer = 0;

        for (int startPointer = 0; startPointer < n; startPointer++) {
            if (startTimes[startPointer] < endTimes[endPointer]) {
                rooms++;
                endPointer++;
            }
        }

        return rooms;
    }
}
