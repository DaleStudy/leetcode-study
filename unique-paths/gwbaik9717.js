// m: height of grid, n: width of grid
// Time complexity: O(m*n)
// Space complexity: O(m*n)

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
  const dp = Array.from({ length: m }, () =>
    Array.from({ length: n }, () => 0)
  );

  dp[0][0] = 1;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (i >= 1) {
        dp[i][j] += dp[i - 1][j];
      }

      if (j >= 1) {
        dp[i][j] += dp[i][j - 1];
      }
    }
  }

  return dp.at(-1).at(-1);
};
