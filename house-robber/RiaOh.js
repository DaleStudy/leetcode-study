/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length <= 1) {
    if (nums.length === 0) {
      return 0;
    } else {
      return nums[0];
    }
  }

  const arr = new Array(nums.length + 1);
  arr[0] = 0;
  arr[1] = nums[0];
  for (let i = 2; i < arr.length; i++) {
    arr[i] = Math.max(arr[i - 1], arr[i - 2] + nums[i - 1]);
  }
  return arr[arr.length - 1];
};
