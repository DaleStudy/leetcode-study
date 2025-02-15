/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 * 
 * 접근 
 * dynamic programming으로 접근
 * 초기 점화식 : dp[i][j] = dp[i-1][j] + dp[i][j-1]
 * 하지만 1차원만 사용해도 되기 때문에 1차원으로 접근
 * 
 * complexity
 * time: O(m*n)
 * space: O(n)
 */
var uniquePaths = function (m, n) {
  const dp = Array(n).fill(1);
  for (let i = 1; i < m; ++i) {
      for (let j = 1; j < n; ++j) {
          dp[j] += dp[j - 1];
      }
  }
  return dp[n - 1];
};

