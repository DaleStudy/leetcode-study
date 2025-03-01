/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

// ✅ Iterative Binary Search for Rotated Sorted Array
// Time Complexity: O(log N)
// Space Complexity: O(1)
var search = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let pointer = Math.floor((left + right) / 2);

    if (nums[pointer] === target) {
      return pointer;
    }

    // Check if the left half is sorted
    if (nums[left] <= nums[pointer]) {
      // Target is in the sorted left half
      if (nums[left] <= target && target < nums[pointer]) {
        right = pointer - 1;
      } else {
        // Target is not in the left half, so search in the right half
        left = pointer + 1;
      }
    } else {
      // The right half must be sorted

      // Target is in the sorted right half
      if (nums[pointer] < target && target <= nums[right]) {
        left = pointer + 1;
      } else {
        // Target is not in the right half, so search in the left half
        right = pointer - 1;
      }
    }
  }

  return -1;
};

