/**
 * 문제 설명
 * - 배열에서 연속된 부분 배열의 곱이 가장 큰 값을 찾는 문제
 *
 * 아이디어
 * - 1) 브루트포스 O(n^2)
 * - 2) DP 최적화 O(n)
 *   - 매 index마다, 현재까지 max 곱, min 곱을 찾고 최대값을 갱신
 */
function maxProduct(nums: number[]): number {
  let maxSoFar = nums[0];
  let max = nums[0];
  let min = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const candidate = [nums[i], max * nums[i], min * nums[i]];
    max = Math.max(...candidate);
    min = Math.min(...candidate);
    maxSoFar = Math.max(maxSoFar, max);
  }
  return maxSoFar;
}
