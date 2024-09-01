/**
 * @description
 * brainstorming:
 * hash map
 *
 * time complexity: O(n)
 * space complexity: O(n)
 */
var missingNumber = function (nums) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    map.set(nums[i], i);
  }

  for (let i = 0; i <= nums.length; i++) {
    if (!map.has(i)) return i;
  }
};
