/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const map = new Map();

  for (let num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
  }

  for (let [_, count] of map) {
    if (count > 1) return true;
  }

  return false;
};

// set 방식으로도 대체가능
// var containsDuplicate = function(nums) {
//     return new Set(nums).size !== nums.length;
// };
