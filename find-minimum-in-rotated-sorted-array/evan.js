/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  let [left, right] = [0, nums.length - 1];

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[right]) {
      // the smallest element is in the right half
      left = mid + 1;
    } else {
      //  the smallest element is in the left half or at mid
      right = mid;
    }
  }

  return nums[left];
};

/**
 * The time complexity of this approach is O(log n), where n is the number of elements in the array.
 * This is because we are effectively halving the search space in each step of the binary search.
 */
