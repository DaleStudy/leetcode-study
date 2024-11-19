/**
 * https://leetcode.com/problems/house-robber-ii
 * T.C. O(n)
 * S.C. O(1)
 */
function rob(nums: number[]): number {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);
  if (nums.length === 3) return Math.max(nums[0], nums[1], nums[2]);

  function robHelper(nums: number[]): number {
    let prev = 0;
    let curr = 0;
    for (let i = 0; i < nums.length; i++) {
      const temp = curr;
      curr = Math.max(prev + nums[i], curr);
      prev = temp;
    }
    return curr;
  }

  const robFirst = robHelper(nums.slice(0, nums.length - 1));
  const robLast = robHelper(nums.slice(1));

  return Math.max(robFirst, robLast);
}
