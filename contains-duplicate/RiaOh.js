/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let count = [nums[0]];
  for (let i = 1; i < nums.length; i++) {
    if (count.includes(nums[i])) {
      return true;
    } else {
      count.push(nums[i]);
    }
  }
  return false;
};
