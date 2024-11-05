/**
 * https://leetcode.com/problems/house-robber
 * T.C. O(n)
 * S.C. O(1)
 */
function rob(nums: number[]): number {
  let prev = 0;
  let curr = 0;
  for (let i = 0; i < nums.length; i++) {
    const temp = curr;
    curr = Math.max(prev + nums[i], curr);
    prev = temp;
  }
  return curr;
}
