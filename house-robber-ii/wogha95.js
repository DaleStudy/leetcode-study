/**
 * TC: O(N)
 * SC; O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length < 4) {
    return Math.max(...nums);
  }

  let prevprevprev = nums[0];
  let prevprev = nums[1];
  let prev = nums[0] + nums[2];

  for (let index = 3; index < nums.length - 1; index++) {
    const current = Math.max(prevprevprev, prevprev) + nums[index];

    prevprevprev = prevprev;
    prevprev = prev;
    prev = current;
  }

  const resultWithoutLast = Math.max(prevprevprev, prevprev, prev);

  prevprevprev = nums[1];
  prevprev = nums[2];
  prev = nums[1] + nums[3];

  for (let index = 4; index < nums.length; index++) {
    const current = Math.max(prevprevprev, prevprev) + nums[index];

    prevprevprev = prevprev;
    prevprev = prev;
    prev = current;
  }

  const resultWithoutFirst = Math.max(prevprevprev, prevprev, prev);

  return Math.max(resultWithoutLast, resultWithoutFirst);
};
