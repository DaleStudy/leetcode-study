/**
 * 요구사항
 * answer이라는 새로운 배열을 만들어야 한다.
 * 이 배열에서 answer[i]는
 * nums[i] 자기 자신을 제외한 나머지 모든 원소들의 곱이 되어야 한다.
 *
 * 풀이
 * 자기 자신을 제외한 곱 = 자기 왼쪽까지의 곱 x 자기 오른쪽 까지의 곱
 * => 왼쪽 누적 곱 x 오른쪽 누적 곱 = answer
 * O(n) time, O(1) space
 */

function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const result: number[] = new Array(n).fill(n);

  let leftProduct = 1;
  for (let i = 0; i < n; i++) {
    result[i] = leftProduct;
    leftProduct *= nums[i];
  }

  let rightProduct = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] *= rightProduct;
    rightProduct *= nums[i];
  }
  return result;
}
