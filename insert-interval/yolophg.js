// Time Complexity: O(n log n)
// Space Complexity: O(n)

var insert = function (intervals, newInterval) {
  // append the newInterval to the intervals array
  intervals.push(newInterval);

  // sort the intervals array by start time
  intervals.sort((a, b) => a[0] - b[0]);

  // to store merged intervals
  let result = [];

  // iterate through the sorted intervals array
  for (let i = 0; i < intervals.length; i++) {
    // if the result array is empty or the current interval does not overlap with the last interval
    if (result.length === 0 || result[result.length - 1][1] < intervals[i][0]) {
      result.push(intervals[i]); // Add the current interval to the result array
    } else {
      // if there is an overlap, merge the current interval with the last interval
      result[result.length - 1][1] = Math.max(
        result[result.length - 1][1],
        intervals[i][1]
      );
    }
  }

  // return the final merged intervals
  return result;
};
