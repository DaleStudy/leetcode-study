/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let map = new Map();
  for (let idx = 0; idx < nums.length; idx++) {
    const rest = target - nums[idx];
    if (map.has(rest)) {
      return [map.get(rest), idx];
    }
    map.set(nums[idx], idx);
  }
  return [];
};

console.log(twoSum([2, 11, 15, 7], 9));
