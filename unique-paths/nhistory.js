var uniquePaths = function (m, n) {
  // Edge case
  if (m === 1 || n === 1) return 1;

  let rowArr = new Array(n).fill(1);

  for (let row = 1; row < m; row++) {
    for (let col = 1; col < n; col++) {
      rowArr[col] += rowArr[col - 1];
    }
  }
  return rowArr[n - 1];
};

// TC: O(m*n)
// SC: O(n)
