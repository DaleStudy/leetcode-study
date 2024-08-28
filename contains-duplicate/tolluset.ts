/*
 * TC: O(n)
 * SC: O(n)
 * */
function containsDuplicate(nums: number[]): boolean {
  return nums.length !== new Set(nums).size;
}
