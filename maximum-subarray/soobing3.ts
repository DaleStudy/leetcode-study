function maxSubArray(nums: number[]): number {
  let max = nums[0];
  const dp = new Array(nums.length).fill(0);
  dp[0] = Math.max(0, nums[0]);

  for(let i = 1; i < nums.length; i++) {
      dp[i] = Math.max(dp[i-1] + nums[i], nums[i]);
      max = Math.max(dp[i], max);
  }
  return max;
};
