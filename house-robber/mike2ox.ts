/**
 * Source: https://leetcode.com/problems/house-robber/
 * 풀이방법: DP를 이용하여 집을 털 때 최대값을 구함
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 *
 * 생각나는 풀이방법
 */
function rob(nums: number[]): number {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  const dp: number[] = new Array(nums.length);

  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  // 남은 집을 순회하면서 최대값을 구함
  for (let i = 2; i < nums.length; i++)
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);

  return dp[nums.length - 1];
}
