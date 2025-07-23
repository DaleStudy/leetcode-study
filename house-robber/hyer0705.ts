// 0ms
function rob(nums: number[]): number {
  const n = nums.length;

  if (n === 1) return nums[0];
  if (n === 2) return Math.max(nums[0], nums[1]);

  const dp: number[] = Array(n).fill(0);
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < n; i++) {
    dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
  }

  return dp[n - 1];
}

// 1ms
/*
function rob(nums: number[]): number {
  const n = nums.length;

  const dp: number[][] = Array.from({ length: n }, () => Array(2).fill(0));

  dp[0][1] = nums[0];

  for (let i = 1; i < n; i++) {
    dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
    dp[i][1] = dp[i - 1][0] + nums[i];
  }

  return Math.max(...dp[n - 1]);
}
*/
