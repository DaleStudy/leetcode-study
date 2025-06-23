/**
 * @param intervals: an array of meeting time intervals
 * @return: if a person could attend all meetings
 */
const canAttendMeetings = function (intervals) {
  intervals.sort((a, b ) =>  a[0] - b[0]); // 시작 시간 기준으로 오름차순 정렬
  
  let prevEnd = intervals[0][1];
  for (const [start, end] of intervals) {
    if (start < prevEnd) {
      return false;
    }
    prevEnd = end;
  }

  return true;
}

// 시간복잡도: O(n * log n)
// 공간복잡도: O(1)
