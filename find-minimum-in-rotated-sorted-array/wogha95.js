/**
 * TC: O(log N)
 * 이진탐색으로 log N으로 계산
 *
 * SC: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  // case1: v_left <= v_center < v_right => return left
  // case2: v_right < v_left <= v_center => left = center
  // case3: v_center < v_right < v_left => right = center

  while (left < right) {
    const center = Math.floor((left + right) / 2);

    if (nums[left] <= nums[center] && nums[center] < nums[right]) {
      return nums[left];
    }
    if (nums[right] < nums[left] && nums[left] <= nums[center]) {
      left = center + 1;
      continue;
    }
    if (nums[center] < nums[right] && nums[right] < nums[left]) {
      right = center;
      continue;
    }
  }

  return nums[left];
};
