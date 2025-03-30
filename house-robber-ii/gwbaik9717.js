// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 1) {
    return nums[0];
  }

  // include first
  const dp1 = Array.from({ length: nums.length + 1 }, () => 0);
  dp1[1] = nums[0];

  // exclude first
  const dp2 = Array.from({ length: nums.length + 1 }, () => 0);

  for (let i = 2; i <= nums.length; i++) {
    dp1[i] = Math.max(dp1[i - 2] + nums[i - 1], dp1[i - 1]);
    dp2[i] = Math.max(dp2[i - 2] + nums[i - 1], dp2[i - 1]);
  }

  return Math.max(dp1.at(-2), dp2.at(-1));
};
