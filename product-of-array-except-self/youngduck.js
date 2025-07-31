/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const numsLength = nums.length;

  const result = new Array(numsLength).fill(1);

  let left = 1;
  let right = 1;

  for (let i = 0; i < numsLength; i++) {
    result[i] *= left;
    left *= nums[i];

    result[numsLength - i - 1] *= right;
    right *= nums[numsLength - i - 1];
  }

  // TC: O(n), SC: O(1)

  return result;
};

console.log(productExceptSelf([1, 2, 3, 4]));
