/**
 * @param {number[]} nums
 * @return {boolean}
 */

// for loof: O(n)
var containsDuplicate = function (nums) {
  let indices = {};
  nums.forEach((num, index) => {
    indices[num] = index;
  });

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in indices && indices[nums[i]] !== i) return true;
  }

  return false;
};

// size 속성: O(1)
var containsDuplicate = function (nums) {
  const indices = new Set(nums);

  if (indices.size !== nums.length) return true;

  return false;
};
