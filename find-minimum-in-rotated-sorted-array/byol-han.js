/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    let mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[right]) {
      // 최소값은 mid 오른쪽
      left = mid + 1;
    } else {
      // 최소값은 mid 포함 왼쪽
      right = mid;
    }
  }

  return nums[left];
};
