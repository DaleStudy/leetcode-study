function findMin(nums: number[]): number {
  const n = nums.length;

  let l = 0;
  let r = n - 1;

  while (l < r) {
    const mid = Math.floor((l + r) / 2);

    if (nums[r] >= nums[mid]) {
      r = mid;
    } else if (nums[r] < nums[mid]) {
      l = mid + 1;
    }
  }

  return nums[l];
}
