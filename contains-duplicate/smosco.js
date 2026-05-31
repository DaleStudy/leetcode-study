/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = (nums) => {
  let uniqueNumSet = new Set(nums);
  return uniqueNumSet.size !== nums.length;
};
