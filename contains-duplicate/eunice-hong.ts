
/**
 * Determines if the array contains any duplicate values.
 * Uses a Set to track seen numbers for O(n) time complexity.
 *
 * @param nums - An array of integers.
 * @returns `true` if there are duplicates, `false` otherwise.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
function containsDuplicate(nums: number[]): boolean {
  let numSet = new Set(nums);
  return numSet.size != nums.length;
};