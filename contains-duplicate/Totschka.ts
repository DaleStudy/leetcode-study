// https://leetcode.com/problems/contains-duplicate/
function containsDuplicate(nums: number[]): boolean {
  const counter = {};
  for (const n of nums) {
    if (!counter[n]) {
      counter[n] = 1;
    } else {
      return true;
    }
  }
  return false;
}
