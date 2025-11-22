function rob(nums: number[]): number {
  const memo = new Array(nums.length).fill(-1);

  function dp(n: number) {
    if (n < 0) {
      return 0;
    }
    if (memo[n] !== -1) {
      return memo[n];
    }
    memo[n] = Math.max(dp(n - 1), dp(n - 2) + nums[n]);
    return memo[n];
  }

  return dp(nums.length - 1);
}
