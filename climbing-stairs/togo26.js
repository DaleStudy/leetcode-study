/**
 * @param {number} n
 * @return {number}
 */

// TC: O(n) / SC: O(n)
var climbStairs = function (n) {
  if (n <= 3) return n;
  const dp = [1, 2, 3];
  for (let i = 3; i < n; i++) {
    dp[i] = dp[i - 2] + dp[i - 1];
  }

  return dp[dp.length - 1];
};

// TC: O(n) / SC: O(1)
var climbStairs = function (n) {
  let temp,
    pre1 = 1,
    pre2 = 1;
  for (let i = 1; i < n; i++) {
    temp = pre2;
    pre2 = pre1 + pre2;
    pre1 = temp;
  }
  return pre2;
};
