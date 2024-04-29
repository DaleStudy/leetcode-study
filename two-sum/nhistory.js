/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  // 1. Make a Hashmap to store { key(index) : value(target-num)}
  let map = {};
  // 2. Iterate to find value is equal to (target - nums[i])
  // There is only one solution
  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    // 3. If there is an index that has different value, return array
    if (diff in map) return [map[diff], i];
    map[nums[i]] = i;
  }
};

// TC: O(n)
// SC: O(n)

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 2, 4], 6));
