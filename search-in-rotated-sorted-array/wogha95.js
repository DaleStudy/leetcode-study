/**
 * TC: O(log N)
 * 이진탐색을 이용하여 순회합니다.
 *
 * SC: O(1)
 * 이진탐색에 이용되는 투 포인터의 공간복잡도를 갖습니다.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  if (nums.length === 1) {
    return target === nums[0] ? 0 : -1;
  }

  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const center = Math.floor((left + right) / 2);
    if (target === nums[left]) {
      return left;
    }
    if (target === nums[center]) {
      return center;
    }
    if (target === nums[right]) {
      return right;
    }

    if (nums[left] <= nums[center] && nums[center] < nums[right]) {
      if (target < nums[left] || nums[right] < target) {
        return -1;
      } else if (nums[left] < target && target < nums[center]) {
        right = center;
      } else if (nums[center] < target && target < nums[right]) {
        left = center + 1;
      }
    } else if (nums[right] < nums[left] && nums[left] <= nums[center]) {
      if (nums[right] < target && target < nums[left]) {
        return -1;
      } else if (nums[left] < target && target < nums[center]) {
        right = center;
      } else {
        left = center + 1;
      }
    } else if (nums[center] < nums[right] && nums[right] < nums[left]) {
      if (nums[center] < target && target < nums[right]) {
        left = center + 1;
      } else if (nums[right] < target && target < nums[left]) {
        return -1;
      } else {
        right = center;
      }
    }
  }

  return -1;
};
