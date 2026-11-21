// 시간 복잡도: O(n)
// 공간 복잡도: O(1) (결과 배열 제외)

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let result = [];
  let product = 1;

  for (let i = 0; i < nums.length; i++) {
    result[i] = product;
    product *= nums[i];
  }

  product = 1;

  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= product;
    product *= nums[i];
  }

  return result;
};
