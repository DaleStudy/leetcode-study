/**
 * @description
 * brainstorming:
 * 1. dfs -> time limited
 * 2. dynamic programming
 *
 * time complexity: O(m * n)
 * space complexity: O(m * n)
 */

var uniquePaths = function (m, n) {
  // initialize
  const dp = Array.from({ length: m }, (_, i) =>
    Array.from({ length: n }, (_, j) => (i === 0 || j === 0 ? 1 : 0))
  );

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      // recurrence relation
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }

  return dp[m - 1][n - 1];
};
