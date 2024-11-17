/**
 * dp[n] = n위치의 집을 훔친다는 가정하에 n위치의 집까지 최대로 훔친 금액
 * dp[n] = Math.max(dp[n - 3], dp[n - 2]) + nums[index]
 *
 * TC: O(N)
 * SC: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length < 3) {
    return Math.max(...nums);
  }

  let prevprevprev = nums[0];
  let prevprev = nums[1];
  let prev = nums[0] + nums[2];

  for (let index = 3; index < nums.length; index++) {
    const current = Math.max(prevprevprev, prevprev) + nums[index];

    prevprevprev = prevprev;
    prevprev = prev;
    prev = current;
  }

  return Math.max(prevprevprev, prevprev, prev);
};
