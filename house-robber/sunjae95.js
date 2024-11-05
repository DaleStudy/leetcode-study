/**
 * @description
 * 최대한 많은 양의 돈이라는 문구에서 dynamic programming을 연상
 * 연속된 집은 털 수 없다라는 문구에서 점화식을 도출 할 수 있었음
 *
 * n = length of nums
 * time complexity: O(n)
 * space complexity: O(n)
 */
var rob = function (nums) {
  if (nums.length === 1) return nums[0];

  const dp = Array(nums.length).fill(0);

  dp[0] = nums[0];
  dp[1] = Math.max(nums[1], dp[0]);

  for (let i = 2; i < nums.length; i++)
    dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);

  return dp[nums.length - 1];
};
