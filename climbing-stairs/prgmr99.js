/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const memo = {};

  function fibo(num, memo) {
    if (num === 1) return 1;
    if (num === 2) return 2;

    if (memo[num]) {
      return memo[num];
    }

    const result = fibo(num - 1, memo) + fibo(num - 2, memo);
    memo[num] = result;

    return result;
  }

  return fibo(n, memo);
};
