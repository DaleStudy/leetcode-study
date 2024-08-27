/**
 * @description
 * brainstorming:
 * 1. O(n^2) brute force
 * 2. hash table
 */

/**
 * @description brainstorming 1 solve
 * time complexity: O(n^2)
 * space complexity: O(n)
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
};

/**
 * @description brainstorming 2 solve
 * time complexity: O(n^2)
 * space complexity: O(n)
 */
var twoSum = function (nums, target) {
  const map = new Map();

  nums.forEach((num, index) => {
    if (!map.get(num)) return map.set(num, [index]);

    map.set(num, map.get(num).concat(index));
  });

  for (let i = 0; i < nums.length; i++) {
    const rest = target - nums[i];

    if (!map.get(rest)) continue;

    const indexList = map.get(rest);
    for (let j = 0; j < indexList.length; j++) {
      if (i === indexList[j]) continue;

      return [i, indexList[j]];
    }
  }
};
