/**
 * @param {number[]} nums
 * @return {boolean}
 */

var containsDuplicate = function(nums) {
  const originalLength = nums.length;
  const parsedLength = new Set(nums).size;

  return originalLength !== parsedLength;
};
