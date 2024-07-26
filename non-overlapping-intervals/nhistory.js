var eraseOverlapIntervals = function (intervals) {
  let count = 0;
  intervals.sort((a, b) => a[1] - b[1]);
  let currentEnd = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    if (currentEnd > intervals[i][0]) {
      count++;
    } else {
      currentEnd = intervals[i][1];
    }
  }

  return count;
};

// TC: O(nlogn)
// SC: O(1)
