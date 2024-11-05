/**
 * https://leetcode.com/problems/meeting-rooms
 * T.C. O(nlogn)
 * S.C. O(1)
 */
function canAttendMeetings(intervals: number[][]): boolean {
  intervals.sort((a, b) => a[0] - b[0]);
  for (let i = 0; i < intervals.length - 1; i++) {
    if (intervals[i][1] > intervals[i + 1][0]) return false;
  }
  return true;
}
