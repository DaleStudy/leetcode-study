/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const result = new Array(nums.length).fill(1); // 결과값

  // 왼쪽 곱 계산
  let leftProduct = 1;
  for (let i = 0; i < nums.length; i++) {
    result[i] = leftProduct;
    leftProduct *= nums[i];
  }

  // 오른쪽 곱 계산해서 왼쪽 곱 계산한거 곱해주기
  let rightProduct = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= rightProduct;
    rightProduct *= nums[i];
  }

  return result;
};

// 조건에 O(n)이라고 있음
// 시간 복잡도: O(n)
// 공간 복잡도: O(n)
