/**
 * @param {number} n
 * @return {number}
 */

var climbStairs = function (n, memo = []) {
  if (memo[n] !== undefined) return memo[n];

  if (n <= 1) return 1;

  memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo);

  return memo[n];
};
