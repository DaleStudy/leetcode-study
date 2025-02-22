// Time complexity: O(logn)
// Space complexity: O(1)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums.at(mid) === target) {
      return mid;
    }

    // rotate 된 구간이 있을 때
    if (nums.at(mid + 1) > nums.at(right)) {
      if (nums.at(right) >= target || nums.at(mid + 1) <= target) {
        left = mid + 1;
        continue;
      }

      right = mid - 1;
      continue;
    }

    if (target >= nums.at(mid + 1) && target <= nums.at(right)) {
      left = mid + 1;
      continue;
    }

    right = mid - 1;
  }

  return -1;
};
