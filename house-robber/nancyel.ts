/**
 * time complexity: O(n) - iterate over a loop
 * space complexity: O(n) - dp array
 *
 * comment: initial naive implementation: simple odd/even alternation, which may return result that is "accidentally correct."
 */
function rob(nums: number[]): number {
  // early return
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  const dp: number[] = new Array(nums.length);
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    // select either 1) current + best from 2 houses ago or 2) skip current, best from previous
    dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
  }

  return dp[nums.length - 1]; // max money from all houses
}
