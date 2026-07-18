/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
function maxSubArray1(nums: number[]): number {
  const dp = new Array(nums.length).fill(0);
  dp[0] = nums[0];

  for (let i = 1; i < nums.length; i++) {
    dp[i] += Math.max(dp[i - 1] + nums[i], nums[i]);
  }
  return Math.max(...dp);
}

/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */
function maxSubArray2(nums: number[]): number {
  let max = nums[0];
  let current = nums[0];

  for (let i = 1; i < nums.length; i++) {
    current = Math.max(current + nums[i], nums[i]);
    max = Math.max(max, current);
  }
  return max;
}
