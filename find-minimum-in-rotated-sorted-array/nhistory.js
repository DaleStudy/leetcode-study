/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  // Make two pointer to find out mid index point and compare values
  let left = 0,
    right = nums.length - 1;

  // If left value of nums is smaller than right value, return left value
  if (nums[left] < nums[right]) return nums[left];

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    // If mid value is greater than last value, left pointer move into next index of mid
    if (nums[mid] > nums[right]) left = mid + 1;
    // Else change right pointer into mid index
    else right = mid;
  }
  return nums[left];
};

// TC: O(log n)
// SC: O(1)
