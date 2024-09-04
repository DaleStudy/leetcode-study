/**
 * https://leetcode.com/problems/maximum-product-subarray
 * T.C. O(n)
 * S.C. O(1)
 * All numbers are integers, so multiplying two numbers cannot result in a smaller absolute value.
 * It's important to pay attention to zeros and negative numbers.
 */
function maxProduct(nums: number[]): number {
  if (nums.length === 0) return 0;

  let max = nums[0];
  let min = nums[0];
  let result = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const num = nums[i];
    if (num < 0) [max, min] = [min, max];

    max = Math.max(num, max * num);
    min = Math.min(num, min * num);

    result = Math.max(result, max);
  }

  return result;
}
