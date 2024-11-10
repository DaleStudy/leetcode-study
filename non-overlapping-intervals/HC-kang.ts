/**
 * https://leetcode.com/problems/non-overlapping-intervals
 * T.C. O(n logn)
 * S.C. O(1)
 * 
 * [[1,2],[2,3],[3,4],[1,3]] =(sort by end)=> [[1,2],[2,3],[1,3],[3,4]]
 * 
 *    0 1 2 3 4...
 *      [=)      pass
 *        [=)    pass
 *      [===)    count++
 *      ^^^
 *          [=)  pass
 */
function eraseOverlapIntervals(intervals: number[][]): number {
  intervals.sort((a, b) => a[1] - b[1]);

  let count = 0;
  let end = -Infinity;

  for (let i = 0; i < intervals.length; i++) {
    if (intervals[i][0] < end) { // 
      count++;
    } else {
      end = intervals[i][1];
    }
  }
  return count;
}
