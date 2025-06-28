// TC: O(n)
// SC: O(n)
function insert(intervals: number[][], newInterval: number[]): number[][] {
  const result: number[][] = [];
  const n = intervals.length;
  let i = 0;

  // Add all intervals that come before newInterval
  while (i < n && intervals[i][1] < newInterval[0]) {
    result.push(intervals[i]);
    i++;
  }

  // Merge all overlapping intervals with newInterval
  while (i < n && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
    newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
    i++;
  }

  result.push(newInterval);

  // Add remaining intervals after newInterval
  while (i < n) {
    result.push(intervals[i]);
    i++;
  }

  return result;
}

