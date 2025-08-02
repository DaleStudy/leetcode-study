function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const result = Array(n).fill(1);

  for (let i = 1; i < n; i++) {
    result[i] = nums[i - 1] * result[i - 1];
  }

  let suffixProduct = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] = result[i] * suffixProduct;
    suffixProduct *= nums[i];
  }

  return result;
}
