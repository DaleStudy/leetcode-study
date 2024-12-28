/**
 * 238. Product of Array Except Self
 * Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 *
 * https://leetcode.com/problems/product-of-array-except-self/description/
 */

// O(n) time
// O(1) space
function productExceptSelf(nums: number[]): number[] {
  const result = new Array(nums.length).fill(1);

  let left = 1;
  for (let i = 0; i < nums.length - 1; i++) {
    left *= nums[i];
    result[i + 1] *= left;
  }

  let right = 1;
  for (let i = nums.length - 1; i > 0; i--) {
    right *= nums[i];
    result[i - 1] *= right;
  }

  return result;
}
