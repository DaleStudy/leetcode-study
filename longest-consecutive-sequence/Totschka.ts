// https://leetcode.com/problems/longest-consecutive-sequence/
function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) {
    return 0;
  }
  nums = [...new Set(nums)].sort((a, b) => a - b);
  let ans = 0;
  let left = 0, right = 1;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] + 1 === nums[i + 1]) {
      ans = Math.max(ans, right - left);
    } else {
      left = right;
    }
    right++;
  }
  return ans + 1;
}
