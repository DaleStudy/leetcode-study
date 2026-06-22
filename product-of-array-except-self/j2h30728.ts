function productExceptSelf(nums: number[]): number[] {
  const length = nums.length;
  const result = new Array(nums.length).fill(1);

  let leftTemp = 1;
  for (let i = 0; i < length; i++) {
    result[i] = leftTemp;
    leftTemp *= nums[i];
  }

  let rightTemp = 1;
  for (let i = length - 1; i >= 0; i--) {
    result[i] *= rightTemp;
    rightTemp *= nums[i];
  }

  return result;
}
