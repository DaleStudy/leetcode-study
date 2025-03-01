// Time complexity: O(nlogn)
// Space complexity: O(1)

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  intervals.sort((a, b) => {
    if (a[0] === b[0]) {
      return a[1] - b[1];
    }

    return a[0] - b[0];
  });

  let count = 0;
  let prevEnd = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    const [start, end] = intervals[i];

    // 구간이 겹칠 때
    if (prevEnd > start) {
      count++;
      prevEnd = Math.min(prevEnd, end);
      continue;
    }

    // 구간이 겹치지 않을 때
    prevEnd = end;
  }

  return count;
};
