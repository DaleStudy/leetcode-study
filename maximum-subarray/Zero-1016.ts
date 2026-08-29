/**
 * 시간 복잡도 O(n)
 * 공간 복잡도 O(1)
 */
function maxSubArray(nums: number[]): number {
  let currentSum = 0;
  let maxSum = -Infinity;

  for (let i = 0; i < nums.length; i++) {
    let n = nums[i];

    currentSum = Math.max(currentSum + n, n);
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
}
