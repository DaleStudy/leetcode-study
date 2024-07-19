// Time Complexity: O(m * n) m : the number of rows, n : the number of columns
// Space Complexity: O(m * n)

var uniquePaths = function (m, n) {
  // dp[i][j] will store the number of unique paths to reach the cell (i, j)
  let dp = Array.from({ length: m }, () => Array(n).fill(1));

  // iterate through the grid starting from (1, 1)
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      // to reach (i-1, j) and (i, j-1) because the robot can only move down or right
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }

  // the value at the bottom-right corner of the grid is the number of unique paths
  return dp[m - 1][n - 1];
};
