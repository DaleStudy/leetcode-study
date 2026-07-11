function climbStairs(n) {
  const memo = {};

  function dp(k) {
    if (k === 1) return 1;
    if (k === 2) return 2;
    if (memo[k]) return memo[k];
    memo[k] = dp(k - 1) + dp(k - 2);
    return memo[k];
  }

  return dp(n);
}
