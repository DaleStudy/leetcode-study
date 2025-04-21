/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const arr = [1, 2];
  for (let i = 2; i <= n - 1; i++) {
    arr[i] = arr[i - 2] + arr[i - 1];
  }
  return arr[n - 1];
};
