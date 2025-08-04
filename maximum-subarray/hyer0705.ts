function maxSubArray(nums: number[]): number {
  const numsLen = nums.length;
  let currentSum = nums[0];
  let maxSum = nums[0];

  for (let i = 1; i < numsLen; i++) {
    currentSum = Math.max(currentSum + nums[i], nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
}
