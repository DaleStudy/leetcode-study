var findMin = function (nums) {
  let left = 0,
    right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[right]) {
      left = mid + 1; // 최솟값이 오른쪽에 있음
    } else {
      right = mid; // 최솟값이 왼쪽에 있음 (mid 포함)
    }
  }

  return nums[left];
};
