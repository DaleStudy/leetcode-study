/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let answer = [];
  answer[0] = 1;

  for (let i = 1; i < nums.length; i++) {
    answer[i] = answer[i - 1] * nums[i - 1];
  }
  let right = 1;

  for (let i = nums.length - 1; i >= 0; i--) {
    answer[i] *= right;
    right *= nums[i];
  }
  return answer;
};

productExceptSelf([1, 2, 3, 4]);
productExceptSelf([-1, 1, 0, -3, 3]);
