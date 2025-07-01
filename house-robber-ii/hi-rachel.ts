function rob(nums: number[]): number {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  function rob_linear(nums: number[]): number {
    const size = nums.length;
    const dp = new Array(size).fill(0);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);
    for (let i = 2; i < size; i++) {
      dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
    }
    return dp[dp.length - 1];
  }

  return Math.max(
    rob_linear(nums.slice(0, nums.length - 1)),
    rob_linear(nums.slice(1))
  );
}
