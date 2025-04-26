/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const array = new Array(nums.length).fill(1);

  for (let i = 1; i < nums.length; i++) {
    array[i] = array[i - 1] * nums[i - 1];
  }

  let right = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    array[i] = array[i] * right;
    right *= nums[i];
  }

  return array;
};

console.log(productExceptSelf([1, 2, 3, 4]));
