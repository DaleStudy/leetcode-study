/**
 * https://leetcode.com/problems/missing-number/
 * T.C.: O(n)
 * S.C.: O(1)
 */
function missingNumber(nums: number[]): number {
  let sum = nums.length; // i for 0 to n-1. So, n is missing.
  for (let i = 0; i < nums.length; i++) sum = sum + i - nums[i];
  return sum;
}
