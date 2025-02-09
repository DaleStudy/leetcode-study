/**
 * @param {number[]} nums
 * @return {number}
 */

// Time Complexity: O(n^)
// Space Complexity: O(n)
var lengthOfLIS = function (nums) {
  if (nums.length === 0) {
    return 0;
  }

  let dp = new Array(nums.length).fill(1); // dp[i] will be the length of LIS ending at i

  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j]) {
        // Strictly increasing condition
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return Math.max(...dp); // The length of the longest subsequence
};

