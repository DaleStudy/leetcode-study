/**
 * https://leetcode.com/problems/insert-interval
 * T.C. O(n)
 * S.C. O(n)
 */
function insert(intervals: number[][], newInterval: number[]): number[][] {
  const result: number[][] = [];

  for (const [start, end] of intervals) {
    if (end < newInterval[0]) {
      result.push([start, end]);
    } else if (newInterval[1] < start) {
      result.push(newInterval);
      newInterval = [start, end];
    } else {
      newInterval[0] = Math.min(newInterval[0], start);
      newInterval[1] = Math.max(newInterval[1], end);
    }
  }

  result.push(newInterval);
  return result;
}
