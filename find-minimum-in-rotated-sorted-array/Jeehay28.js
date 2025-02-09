/**
 * @param {number[]} nums
 * @return {number}
 */

// Binary Search
// Time Complexity: O(log n) (Binary search halving the search space each step)
// Space Complexity: O(1) (No extra space except for a few variables)
var findMin = function (nums) {
  // Example Rotations:
  // nums = [0,1,2,4,5,6,7]
  // [4,5,6,7,0,1,2] -> Rotated 4 times
  // [0,1,2,4,5,6,7] -> 7 times rotated

  // Initial State:
  // [4, 5, 6, 7, 0, 1, 2]
  //  ↑                 ↑
  // (left)           (right)
  //
  // Find mid:
  // [4, 5, 6, 7, 0, 1, 2]
  //  ↑       🎯        ↑
  // (left)   (mid)   (right)
  //
  // If nums[mid] > nums[right], move left to search in the right half:
  // [4, 5, 6, 7, 0, 1, 2]
  //              ↑     ↑
  //          (left)   (right)

  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    let mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[right]) {
      // Minimum must be in the right half
      // Need to update left to search in the right half
      left = mid + 1;
    } else {
      // Minimum is in the left half (including mid)
      // Need to update right to search in the left half
      right = mid;
    }
  }

  return nums[left];
};

