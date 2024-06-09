var search = function (nums, target) {
  // Exception case
  if (nums.length === 0) return -1; // There is no element in nums
  if (nums.length === 1) {
    return nums[0] === target ? 0 : -1;
  }

  // Create two pointer: left,right and mid, left = 0, right = nums.length-1
  let left = 0,
    right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[left] === target) return left;
    if (nums[right] === target) return right;
    if (nums[mid] === target) return mid;

    // If left part is sorted, move pointer depends on target position
    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
      // If right part is sorted, move pointer depends on target position
    } else {
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }
  return -1;
};

// TC: O(log n)
// SC: O(1)
