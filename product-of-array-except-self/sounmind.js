/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const length = nums.length;
  const result = Array(length).fill(1);

  let leftProduct = 1;
  for (let i = 0; i < length; i++) {
    result[i] = leftProduct;
    leftProduct *= nums[i];
  }

  let rightProduct = 1;
  for (let i = length - 1; i >= 0; i--) {
    result[i] *= rightProduct;
    rightProduct *= nums[i];
  }

  return result;
};

/**
 * Time Complexity: O(n)
 * The algorithm iterates through the nums array twice (two separate loops), each taking O(n) time.
 * Hence, the overall time complexity is O(2n), which simplifies to O(n).
 *
 * Space Complexity: O(1)
 * The algorithm uses a constant amount of extra space for the leftProduct and rightProduct variables.
 * The result array is not considered extra space as it is required for the output.
 * Therefore, the extra space complexity is O(1).
 */
