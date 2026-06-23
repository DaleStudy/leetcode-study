/**
 * @param {number[]} nums
 * @return {boolean}
 */
function containsDuplicate(nums) {
  let set_nums = new Set(nums);

  if (set_nums.size !== nums.length) return true;
  else return false;
}
