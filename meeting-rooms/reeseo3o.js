// Time Complexity: O(nlogn)
// Space Complexity: O(1)

const canAttendMeetings = function (intervals) {
  if (!intervals || intervals.length <= 1) {
    return true;
  }

  intervals.sort((a, b) => a[0] - b[0]);

  for (let i = 1; i < intervals.length; i++) {
    const prevEnd = intervals[i - 1][1];
    const currStart = intervals[i][0];

    if (currStart < prevEnd) {
      return false;
    }
  }

  return true;
};
