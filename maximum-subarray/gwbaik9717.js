// Time complexity: O(n)
// Space complexity: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  const n = nums.length;
  const dp = [0, 0];

  let answer = Number.MIN_SAFE_INTEGER;

  for (let i = 1; i <= n; i++) {
    if (i % 2 !== 0) {
      dp[1] = Math.max(dp[0] + nums[i - 1], nums[i - 1]);
      answer = Math.max(answer, dp[1]);
    } else {
      dp[0] = Math.max(dp[1] + nums[i - 1], nums[i - 1]);
      answer = Math.max(answer, dp[0]);
    }
  }

  return answer;
};
