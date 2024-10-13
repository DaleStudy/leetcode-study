/**
 * https://leetcode.com/problems/maximum-subarray
 * Kadane's Algorithm
 * T.C. O(n)
 * S.C. O(1)
 */
function maxSubArray(nums: number[]): number {
  let maxSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    nums[i] = Math.max(nums[i], nums[i] + nums[i - 1]);
    maxSum = Math.max(maxSum, nums[i]);
  }

  return maxSum;
}

/**
 * Divide and Conquer version
 * T.C. O(n log n)
 * S.C. O(log n) - call stack
 */
function maxSubArray(nums: number[]): number {
  function maxSubArrayHelper(
    nums: number[],
    left: number,
    right: number
  ): number {
    if (left === right) return nums[left];

    const mid = (left + right) >> 1;
    const leftMax = maxSubArrayHelper(nums, left, mid);
    const rightMax = maxSubArrayHelper(nums, mid + 1, right);
    let leftSum = -Infinity;
    let rightSum = -Infinity;
    let sum = 0;

    for (let i = mid; i >= left; i--) {
      sum += nums[i];
      leftSum = Math.max(leftSum, sum);
    }

    sum = 0;
    for (let i = mid + 1; i <= right; i++) {
      sum += nums[i];
      rightSum = Math.max(rightSum, sum);
    }

    return Math.max(leftMax, rightMax, leftSum + rightSum);
  }

  return maxSubArrayHelper(nums, 0, nums.length - 1);
}

/**
 * Iterative version
 * T.C. O(n log n)
 * S.C. O(log n) - call stack
 */
function maxSubArray(nums: number[]): number {
  const stack = [[0, nums.length - 1]];
  let maxSum = nums[0];

  while (stack.length) {
    const [left, right] = stack.pop()!;
    if (left === right) {
      maxSum = Math.max(maxSum, nums[left]);
      continue;
    }

    const mid = (left + right) >> 1;
    stack.push([left, mid], [mid + 1, right]);

    let leftSum = -Infinity;
    let rightSum = -Infinity;
    let sum = 0;

    for (let i = mid; i >= left; i--) {
      sum += nums[i];
      leftSum = Math.max(leftSum, sum);
    }

    sum = 0;
    for (let i = mid + 1; i <= right; i++) {
      sum += nums[i];
      rightSum = Math.max(rightSum, sum);
    }

    maxSum = Math.max(maxSum, leftSum + rightSum);
  }

  return maxSum;
}
