// Time complexity: O(logn)
// Space complexity: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (nums.at(mid - 1) > nums.at(mid)) {
      return nums[mid];
    }

    if (nums.at(mid + 1) < nums.at(mid)) {
      return nums[mid + 1];
    }

    if (nums.at(mid + 1) > nums.at(right)) {
      left = mid + 1;
      continue;
    }

    right = mid - 1;
  }

  return nums[left];
};
