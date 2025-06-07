/**
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  // Continue searching while the window is valid
  while (left <= right) {
    // Find the middle index
    let mid = Math.floor((left + right) / 2);

    // If the target is found at mid, return the index
    if (nums[mid] === target) {
      return mid;
    }

    // Check if the left half is sorted
    if (nums[left] <= nums[mid]) {
      // If target is in the range of the sorted left half
      if (nums[left] <= target && target < nums[mid]) {
        // Move the right pointer to just before mid
        right = mid - 1;
      } else {
        // Target must be in the right half
        left = mid + 1;
      }

      // Otherwise, the right half must be sorted
    } else {
      // If target is in the range of the sorted right half
      if (nums[mid] < target && target <= nums[right]) {
        // Move the left pointer to just after mid
        left = mid + 1;
      } else {
        // Target must be in the left half
        right = mid - 1;
      }
    }
  }

  // If the loop ends, target is not in the array
  return -1;
};
