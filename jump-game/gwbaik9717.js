// Time complexity: O(n)
// Space complexity: O(1)

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  let maxValue = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (i > maxValue) {
      return false;
    }

    const newNum = i + nums[i];

    if (newNum > maxValue) {
      maxValue = newNum;
    }

    if (maxValue >= nums.length - 1) {
      break;
    }
  }

  return true;
};
