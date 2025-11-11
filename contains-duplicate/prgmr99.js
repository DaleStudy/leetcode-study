/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const numArrLength = nums.length;
  const numSetSize = new Set(nums).size;

  return numArrLength !== numSetSize;
};
