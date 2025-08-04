// https://leetcode.com/problems/meeting-rooms/
// TC: O(N log N), N은 회의의 개수, 회의 시간 정렬 O(N log N)
// SC: O(1)

function canAttendMeetings(intervals: number[][]): boolean {
  intervals.sort((a, b) => a[0] - b[0]);
  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] < intervals[i - 1][1]) {
      return false;
    }
  }
  return true;
}
