/**
 * 구간 내 최대 합을 dp에 저장
 * 시간복잡도 O(n)
 * 공간복잡도 O(n)
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let dp = new Array(nums.length).fill(0);

  dp[0] = nums[0];
  for (let i = 1; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
  }

  return Math.max(...dp);
};
