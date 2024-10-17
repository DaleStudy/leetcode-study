/**
 * @description
 *
 * n = length of nums
 * time complexity: O(n)
 * space complexity: O(1)
 */
var canJump = function (nums) {
  let cur = 1;
  for (const num of nums) {
    if (cur === 0) return false;
    cur--;
    cur = cur > num ? cur : num;
  }

  return true;
};
