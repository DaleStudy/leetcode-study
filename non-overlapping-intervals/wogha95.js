/**
 * TC: O(N * logN)
 * 정렬로 인한 시간복잡도
 *
 * SC: O(1)
 */

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  intervals.sort((a, b) => a[1] - b[1]);

  let count = 0;
  let lastEnd = Number.MIN_SAFE_INTEGER;

  for (const [start, end] of intervals) {
    if (start < lastEnd) {
      count += 1;
    } else {
      lastEnd = end;
    }
  }

  return count;
};
