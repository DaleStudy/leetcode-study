// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const set = new Set(nums);

  return set.size !== nums.length;
};
