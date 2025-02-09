/**
 *
 * 접근 방법 :
 *  - O(n)으로 풀어야 하니까 중첩이 아닌 배열 개별로 2번 순회 방법으로 접근
 *  - 왼쪽 곱(prefixProduct)과 오른쪽 곱((suffixProduct)을 따로 계산해서 결과값에 저장
 *
 * 시간복잡도 : O(n)
 *  - 배열 길이만큼 순회하니까 O(n)
 *
 * 공간복잡도 : O(n)
 *  - 배열 길이만큼 결과값 저장하니까 O(n)
 *
 */

function productExceptSelf(nums: number[]): number[] {
  let result: number[] = Array(nums.length).fill(1);
  let prefixProduct = 1;
  let suffixProduct = 1;

  for (let i = 0; i < nums.length; i++) {
    result[i] = prefixProduct;
    prefixProduct *= nums[i];
  }

  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= suffixProduct;
    suffixProduct *= nums[i];
  }

  return result;
}
