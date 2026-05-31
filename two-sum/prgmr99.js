/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const numMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    const firstNum = nums[i];
    const secondNum = target - nums[i];

    if (numMap.has(secondNum)) {
      return [numMap.get(secondNum), i];
    }

    numMap.set(firstNum, i);
  }
};
