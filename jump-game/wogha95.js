/**
 * TC: O(N)
 * SC: O(1)
 * N: nums.length
 */

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  if (nums.length === 1) {
    return true;
  }

  let maximumIndex = 0;

  for (let index = 0; index < nums.length; index++) {
    const jumpLength = nums[index];

    if (jumpLength === 0) {
      continue;
    }

    if (maximumIndex < index) {
      return false;
    }

    maximumIndex = Math.max(maximumIndex, index + nums[index]);

    if (maximumIndex >= nums.length - 1) {
      return true;
    }
  }

  return false;
};
