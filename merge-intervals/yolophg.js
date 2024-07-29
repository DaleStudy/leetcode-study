// Time Complexity: O(n log n)
// Space Complexity: O(n)

var merge = function (intervals) {
  // sort the intervals by their start time
  intervals.sort((a, b) => a[0] - b[0]);

  // to manage merged intervals
  let stack = [];

  // push the first interval onto the stack
  stack.push(intervals[0]);

  // iterate through the sorted intervals
  for (let i = 1; i < intervals.length; i++) {
    // get the top interval from the stack
    let top = stack[stack.length - 1];

    // if the current interval overlaps with the top interval
    if (top[1] >= intervals[i][0]) {
      // merge the intervals by updating the end of the top interval
      top[1] = Math.max(top[1], intervals[i][1]);
    } else {
      // if there is no overlap, push the current interval onto the stack
      stack.push(intervals[i]);
    }
  }

  // return the final merged intervals
  return stack;
};
