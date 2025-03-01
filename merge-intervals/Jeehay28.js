// 🚀 My own approach!
// ✅ Time Complexity: O(n log n), where n is the number of intervals
// ✅ Space Complexity: O(n) (due to the stack storage)

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  // Sorting takes O(n log n) time, where n is the number of intervals.
  // JavaScript's sort() is O(1) (in-place) for sorting in most cases.

  let start = intervals[0][0];
  let end = intervals[0][1];
  let stack = [intervals[0]]; // O(n) additional space usage.

  for (const [s, e] of intervals) {
    // This takes O(n) time.
    const [prevStart, prevEnd] = stack[stack.length - 1];

    if (prevStart <= s && s <= prevEnd) {
      start = Math.min(s, start);
      end = Math.max(e, end);
      stack.pop();
    } else {
      start = s;
      end = e;
    }
    stack.push([start, end]);
  }
  return stack;
};

