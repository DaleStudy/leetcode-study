/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let nums_length = nums.length;
  let hash = new Set(nums);
  let hash_legnth = hash.size;
  return nums_length === hash_legnth ? false : true;
};

containsDuplicate([1, 2, 3, 1]);
