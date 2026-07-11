// TC: O(n) / SC: O(n)
var productExceptSelf = function (nums) {
  const left = [1];
  const right = [1];
  const result = [];

  for (let i = 1; i < nums.length; i++) {
    left.push(left[i - 1] * nums[i - 1]);
  }

  for (let i = nums.length - 1; i > 0; i--) {
    right.push(right[nums.length - 1 - i] * nums[i]);
  }

  for (let i = 0, j = nums.length - 1; i < nums.length; i++, j--) {
    result[i] = left[i] * right[j];
  }

  return result;
};

// TC: O(n) / SC: O(1)
var productExceptSelf = function (nums) {
  const left = new Array(nums.length).fill(1);

  for (let i = 1; i < nums.length; i++) {
    left[i] = left[i - 1] * nums[i - 1];
  }

  let rightProduct = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    left[i] *= rightProduct;
    rightProduct *= nums[i];
  }

  return left;
};
