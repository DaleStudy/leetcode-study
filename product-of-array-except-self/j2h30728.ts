/**
 * 시간 복잡도 : O(n)
 * 공간 복잡도 : O(n)
 */
function productExceptSelf(nums: number[]): number[] {
  const arr = new Array(nums.length).fill(1);

  let left = 1;
  for (let i = 0; i < nums.length; i++) {
    arr[i] = left;
    left *= nums[i];
  }

  let right = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    arr[i] *= right;
    right *= nums[i];
  }

  return arr;
}
