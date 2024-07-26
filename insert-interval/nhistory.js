var insert = function (intervals, newInterval) {
  let result = [];
  let i = 0;

  // 1. Add all intervals before the new interval
  while (i < intervals.length && intervals[i][1] < newInterval[0]) {
    result.push(intervals[i]);
    i++;
  }

  // 2. Merge all overlapping intervals with new interval
  while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
    i++;
  }
  result.push(newInterval);

  // 3. Add all intervals after the new interval
  while (i < intervals.length && intervals[i][1] >= newInterval[0]) {
    result.push(intervals[i]);
    i++;
  }

  return result;
};

// TC = O(n)
// SC = O(n)
