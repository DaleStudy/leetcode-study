/**
 * 268. Missing Number
 * Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
 *
 * https://leetcode.com/problems/missing-number/description/
 */

// O(n) time
// O(1) space
function missingNumber(nums: number[]): number {
  const n = nums.length;
  let total = (n * (n + 1)) / 2;

  let sum = 0;
  for (let i = 0; i < n; i++) {
    sum += nums[i];
  }

  return total - sum;
}
