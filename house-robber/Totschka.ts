// https://leetcode.com/problems/house-robber/
let dp;
function rob(nums: number[]): number {
  dp = Array.from({ length: nums.length + 1 }, () => -1);
  return doRobbery(nums, nums.length - 1);
}

function doRobbery(nums: number[], i: number) {
  if (i < 0) {
    return 0;
  }
  if (dp[i] >= 0) {
    return dp[i];
  }
  const money = Math.max(doRobbery(nums, i - 2) + nums[i], doRobbery(nums, i - 1));
  dp[i] = money;
  return money;
}
