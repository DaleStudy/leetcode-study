//! 다시 풀어보기 (divide and conquer)
const maxSubArray = function (nums) {
  let currentSum = 0;
  let maxSum = -Infinity;

  for (let right = 0; right < nums.length; right++) {
    currentSum += nums[right];
    maxSum = Math.max(maxSum, currentSum);
    if (currentSum < 0) currentSum = 0;
  }

  return maxSum;
};
