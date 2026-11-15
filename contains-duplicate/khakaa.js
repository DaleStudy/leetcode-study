/**
 * Complexity:
 * - Time: O(n)
 * - Space:	O(n)
 */

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const numSet = new Set(nums);

  return nums.length !== Array.from(numSet).length;
};
