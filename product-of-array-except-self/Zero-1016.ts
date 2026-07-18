/**
 * 시간복잡도 O(n)
 * 공간복잡도 O(n)
 */
function productExceptSelf(nums: number[]): number[] {
  const n_length = nums.length;
  const result = new Array(n_length).fill(1);

  // NOTE: 왼쪽 -> 오른쪽, 오른쪽 -> 왼쪽 순회하면서 값을 누적함.
  let left = 1;
  for (let i = 0; i < n_length; i++) {
    result[i] *= left;
    left *= nums[i];
  }

  let right = 1;
  for (let i = n_length - 1; i >= 0; i--) {
    result[i] *= right;
    right *= nums[i];
  }

  return result;
}
