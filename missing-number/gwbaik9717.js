// Time complexity: O(n)
// Space complexity: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  const n = nums.length;
  const target = (n * (n + 1)) / 2;

  const sum = nums.reduce((a, c) => a + c, 0);

  return target - sum;
};
