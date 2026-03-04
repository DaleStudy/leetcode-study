/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  return  new Set(nums).size != nums.length;
};

// 40ms 80.33MB