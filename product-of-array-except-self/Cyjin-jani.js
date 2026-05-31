// tc : O(n).
// sc : O(n)이지만 출력 배열(result)은 카운트 되지 않는다고 했으므로 O(1).
const productExceptSelf = function (nums) {
  const length = nums.length;
  const result = Array.from({ length }).fill(1);

  let leftSide = 1;
  let rightSide = 1;

  for (let i = 0; i < length; i++) {
    result[i] = leftSide;
    leftSide *= nums[i];
  }

  for (let i = length - 1; i >= 0; i--) {
    result[i] *= rightSide;
    rightSide *= nums[i];
  }

  return result;
};
