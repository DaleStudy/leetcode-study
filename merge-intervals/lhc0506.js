/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
  const sortedIntervals = intervals.toSorted((a, b) => a[0] - b[0]);

  if (intervals.length === 1) {
      return intervals;
  }

  const result = [];
  let [start, end] = sortedIntervals[0];


  for (let i = 1; i < sortedIntervals.length; i++) {
      const [currentStart, currentEnd] = sortedIntervals[i];

      if (currentStart <= end) {
          end = Math.max(end, currentEnd);
      } else {
          result.push([start, end]);
          start = currentStart;
          end = currentEnd;
      }

      if (i === sortedIntervals.length - 1) {
          result.push([start, end]);
      }
  }

  return result;
};

// 시간 복잡도: O(nlogn)
// 공간 복잡도: O(n)
