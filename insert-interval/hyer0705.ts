// Time Complexity: O(n)
// Space Complexity: O(n)
function insert(intervals: number[][], newInterval: number[]): number[][] {
  const result: number[][] = [];
  let merged = newInterval;
  let i = 0;

  while (i < intervals.length && intervals[i][1] < merged[0]) {
    result.push(intervals[i++]);
  }

  while (i < intervals.length && intervals[i][0] <= merged[1]) {
    merged[0] = Math.min(merged[0], intervals[i][0]);
    merged[1] = Math.max(merged[1], intervals[i][1]);
    i++;
  }
  result.push(merged);

  while (i < intervals.length && intervals[i][0] > merged[1]) {
    result.push(intervals[i++]);
  }

  return result;
}
