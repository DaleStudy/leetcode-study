/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  // 1. Make hashmap that has previous value
  let map = {};
  // 2. Iterate nums to check nums[i] is duplicated or not
  for (let i = 0; i < nums.length; i++) {
    // 2.1 Check there is same value on the map
    // 3. Return true when their is duplicated value
    if (nums[i] in map) {
      return true;
    } else map[nums[i]] = i;
  }
  return false;
};

// TC: O(n)
// SC: O(n)

console.log(containsDuplicate([1, 2, 3, 1])); // true
console.log(containsDuplicate([1, 2, 3, 4])); // false
console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])); // true
