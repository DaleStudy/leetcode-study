/**
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
 * T.C. O(log n)
 * S.C. O(1)
 */
function findMin(nums: number[]): number {
  let left = 0;
  let right = nums.length - 1;
  let mid = (left + right) >> 1;

  while (left < right) {
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
    mid = (left + right) >> 1;
  }
  return nums[left];
}
