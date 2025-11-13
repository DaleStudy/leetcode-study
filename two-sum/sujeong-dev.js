/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// 2중 for문: O(n^2)
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (i === j) continue;
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
};

// for loof: O(n)
var twoSum = function (nums, target) {
  let result = {};

  nums.forEach((num, index) => {
    result[num] = index;
  });

  for (let i = 0; i < nums.length; i++) {
    const findNum = target - nums[i];

    if (findNum in result && result[findNum] !== i) {
      return [i, result[findNum]];
    }
  }
};
