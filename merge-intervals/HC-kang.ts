/**
 * https://leetcode.com/problems/merge-intervals
 * T.C. O(n logn)
 * S.C. O(n)
 */
function merge(intervals: number[][]): number[][] {
  intervals.sort((a, b) => a[0] - b[0]); // T.C. O(n logn)

  const result = [intervals[0]]; // S.C. O(n)

  // T.C. O(n)
  for (let i = 1; i < intervals.length; i++) {
    const last = result[result.length - 1];
    const current = intervals[i];

    if (last[1] >= current[0]) {
      last[1] = Math.max(last[1], current[1]);
    } else {
      result.push(current);
    }
  }

  return result;
}
