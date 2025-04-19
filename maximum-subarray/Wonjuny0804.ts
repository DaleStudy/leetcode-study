function maxSubArray(nums: number[]): number {
  const n = nums.length;
  const dp = new Array(n).fill(0);
  dp[0] = nums[0];
  let result = dp[0];

  for (let i = 1; i < n; i++) {
      dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
      result = Math.max(result, dp[i]);
  }

  return result;
}
