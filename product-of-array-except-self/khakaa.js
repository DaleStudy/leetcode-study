/**
 * Complexity:
 * - Time: O(n)
 * - Space:	O(1) (excluding the output array)
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const size = nums.length;
  let answer = [];
  answer[0] = 1;

  for (let i = 1; i < nums.length; i++) {
    answer[i] = answer[i - 1] * nums[i - 1];
  }

  let rightProduct = 1;
  for (let i = size - 1; i >= 0; i--) {
    answer[i] *= rightProduct;
    rightProduct *= nums[i];
  }

  return answer;
};
