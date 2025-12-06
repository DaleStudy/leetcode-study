function findMin(nums: number[]): number {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const middle = Math.floor((left + right) / 2);

    if (nums[middle] < nums[right]) {
      right = middle;
    } else {
      left = middle + 1;
    }
  }
  return nums[left];
}
