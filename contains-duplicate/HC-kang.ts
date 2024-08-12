/**
217. Contains Duplicate

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 */

function containsDuplicate(nums: number[]): boolean {
  return nums.length !== new Set(nums).size;
}
