/**
 * source: https://leetcode.com/problems/product-of-array-except-self/
 * 풀이방법: 왼쪽부터의 누적 곱과 오른쪽부터의 누적 곱을 이용하여 결과 계산
 * 시간복잡도: O(n) (n: nums의 길이)
 * 공간복잡도: O(1) (상수 공간만 사용)
 */
function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const result = new Array(n);

  // 왼쪽부터의 누적 곱 계산
  result[0] = 1;
  for (let i = 1; i < n; i++) {
    result[i] = result[i - 1] * nums[i - 1];
  }

  // 오른쪽부터의 누적 곱을 곱하면서 결과 계산
  let right = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] = result[i] * right;
    right *= nums[i];
  }

  return result;
}
