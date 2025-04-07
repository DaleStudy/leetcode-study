function productExceptSelf(nums: number[]): number[] {
  const left = Array(nums.length).fill(1);
  const right = Array(nums.length).fill(1);
  const result = Array(nums.length);

  for (let i = 1; i < nums.length; i++) {
    left[i] = left[i - 1] * nums[i - 1];
  }

  for (let i = nums.length - 2; i >= 0; i--) {
    right[i] = right[i + 1] * nums[i + 1];
  }

  for (let i = 0; i < nums.length; i++) {
    result[i] = left[i] * right[i];
  }

  return result;
}
