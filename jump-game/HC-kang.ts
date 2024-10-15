/**
 * https://leetcode.com/problems/jump-game/
 * T.C. O(n)
 * S.C. O(1)
 */
function canJump(nums: number[]): boolean {
  let max = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i > max) return false;
    max = Math.max(max, i + nums[i]);
    if (max >= nums.length) return true;
  }

  return false;
}
