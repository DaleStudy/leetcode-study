/**
 * https://leetcode.com/problems/meeting-rooms-ii
 * T.C. O(nlogn)
 * S.C. O(n)
 */
function minMeetingRooms(intervals: number[][]): number {
  const starts = intervals.map((interval) => interval[0]).sort((a, b) => a - b);
  const ends = intervals.map((interval) => interval[1]).sort((a, b) => a - b);

  let rooms = 0;
  let endIdx = 0;
  for (let i = 0; i < starts.length; i++) {
    if (starts[i] < ends[endIdx]) {
      rooms++;
    } else {
      endIdx++;
    }
  }

  return rooms;
}
