// 🚀 Greedy Algorithm
// ✅ Time Complexity: O(n log n), where n is the number of intervals
// - Sorting the intervals: O(n log n)
// - Iterating through intervals: O(n)

// ✅ Space Complexity: O(1), No other data structures are used,

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  // ✅ Sorting by end time ensures that we keep intervals that finish the earliest, reducing the chances of overlap with the subsequent intervals.
  // ❌ Sorting by start time would lead to a greedy choice too early, causing unnecessary removals.
  intervals.sort((a, b) => a[1] - b[1]);

  let removalCnt = 0;

  let prevEnd = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    const [start, end] = intervals[i];

    if (start < prevEnd) {
      removalCnt += 1; // Increment removal count for an overlap
    } else {
      prevEnd = end;
    }
  }
  return removalCnt;
};

