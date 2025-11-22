function productExceptSelf(nums: number[]): number[] {
  const len = nums.length;
  const result = new Array(len).fill(1);
  let pre = 1;
  let post = 1;
  for (let i = 0; i < len; i++) {
    result[i] *= pre;
    pre *= nums[i];

    result[len - i - 1] *= post;
    post *= nums[len - i - 1];
  }
  return result;
}
