var merge = function (intervals) {
  // Sort intervals with first start number
  intervals.sort((a, b) => a[0] - b[0]);
  let result = [];
  let currentInterval = intervals[0];

  for (let i = 1; i < intervals.length; i++) {
    if (currentInterval[1] >= intervals[i][0]) {
      currentInterval[1] = Math.max(currentInterval[1], intervals[i][1]);
    } else {
      result.push(currentInterval);
      currentInterval = intervals[i];
    }
  }

  result.push(currentInterval);

  return result;
};

// TC: O(nlogn)
// SC: O(n)
