/**
 * @param {number[]} nums
 * @return {boolean}
 */

/**
 * Runtime: 89ms, Memory: 63MB
 *
 * Time complexity: O(n)
 *  - To find the length of an array: O(n)
 *  - Array to Set: O(n)
 *  - To find the size of a set: O(n)
 * Space complexity: O(n)
 *  - arrToSet: O(n)
 *
 * **/

var containsDuplicate = function (nums) {
  const arrLength = nums.length;
  const arrToSet = new Set(nums);
  const setLength = arrToSet.size;

  if (arrLength !== setLength) {
    return true;
  }
  return false;
};
