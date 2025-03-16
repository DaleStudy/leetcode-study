// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
  const dp = Array.from({ length: n + 1 }, () => 0);

  if (n === 0) {
    return dp;
  }

  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    const k = Math.floor(Math.log2(i));

    dp[i] = 1 + dp[i - Math.pow(2, k)];
  }

  return dp;
};
