/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  const length = nums.length;

  let left = 0;
  let right = length - 1;
  let result = Infinity;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (nums[mid] < nums[left]) {
      result = Math.min(result, nums[mid]);
      right = mid - 1;
    } else {
      result = Math.min(result, nums[left]);
      left = mid + 1;
    }
  }

  return result;
};
