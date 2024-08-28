// T.C: O(n)
// S.C: O(n)
function productExceptSelf(nums: number[]): number[] {
  const arr: number[] = new Array(nums.length);
  let product = 1;
  for (let i = 0; i < nums.length; i++) {
    arr[i] = product;
    product *= nums[i];
  }

  product = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    arr[i] *= product;
    product *= nums[i];
  }

  return arr;
};
