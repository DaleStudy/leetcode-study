/**
 * Source: https://leetcode.com/problems/maximum-product-subarray/
 * 풀이방법: 현재 곱과 최대 곱을 비교하여 최대값을 구함
 *
 * 시간복잡도: O(n)
 * 공간복잡도: O(1)
 *
 * 다른 풀이방법
 * - DP를 이용하여 풀이
 */
function maxProduct(nums: number[]): number {
  if (nums.length === 0) return 0;

  let maxProduct = nums[0];
  let currentProduct = 1;

  // 왼쪽에서 오른쪽으로 순회
  for (let i = 0; i < nums.length; i++) {
    currentProduct *= nums[i];
    maxProduct = Math.max(maxProduct, currentProduct);
    // 현재 곱이 0이 되면 리셋
    if (currentProduct === 0) {
      currentProduct = 1;
    }
  }

  currentProduct = 1;

  // 오른쪽에서 왼쪽으로 순회
  for (let i = nums.length - 1; i >= 0; i--) {
    currentProduct *= nums[i];
    maxProduct = Math.max(maxProduct, currentProduct);
    // 현재 곱이 0이 되면 리셋
    if (currentProduct === 0) {
      currentProduct = 1;
    }
  }

  return maxProduct;
}
