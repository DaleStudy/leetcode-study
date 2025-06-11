var search = function (nums, target) {
  let left = 0,
    right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) return mid;

    // 왼쪽 절반이 정렬되어 있는 경우
    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1; // 왼쪽 범위로 이동
      } else {
        left = mid + 1; // 오른쪽 범위로 이동
      }
    }
    // 오른쪽 절반이 정렬되어 있는 경우
    else {
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1; // 오른쪽 범위로 이동
      } else {
        right = mid - 1; // 왼쪽 범위로 이동
      }
    }
  }

  return -1;
};
