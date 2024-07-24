// Time Complexity: O(n log n)
// Space Complexity: O(1)

var eraseOverlapIntervals = function (intervals) {
  // sort the intervals based on their end times
  intervals.sort((a, b) => a[1] - b[1]);

  let end = intervals[0][1];
  let count = 0;

  // iterate through the sorted intervals
  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] < end) {
      // overlapping interval found, increment the count
      count++;
    } else {
      // no overlap, update the end to the current interval's end
      end = intervals[i][1];
    }
  }

  return count;
};
