/**
 * https://leetcode.com/problems/house-robber-ii/submissions/1686583649/
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 1) return nums[0];

  // Helper to solve the linear house robber problem
  function robLinear(houses) {
    let prev1 = 0; // dp[i-1]
    let prev2 = 0; // dp[i-2]

    for (let money of houses) {
      let temp = prev1;
      prev1 = Math.max(prev1, prev2 + money);
      prev2 = temp;
    }

    return prev1;
  }

  // Case 1: Exclude last house
  let money1 = robLinear(nums.slice(0, nums.length - 1));
  // Case 2: Exclude first house
  let money2 = robLinear(nums.slice(1));

  return Math.max(money1, money2);
};
