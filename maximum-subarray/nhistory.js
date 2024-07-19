var maxSubArray = function (nums) {
  // Edge case
  if (nums.length === 1) return nums[0];

  let maxSum = nums[0];
  let curSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    curSum = Math.max(nums[i], curSum + nums[i]);
    maxSum = Math.max(maxSum, curSum);
  }

  return maxSum;
};

// TC: O(n)
// SC: O(1)
