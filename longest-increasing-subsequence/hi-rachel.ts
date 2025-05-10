/**
 * 주어진 정수 배열 nums에서 가장 긴 증가하는 부분 수열의 길이를 구하는 문제
 *
 * new Array(n).fill(1) -> 길이가 n인 배열을 만들어, 모든 요소를 1로 채움
 *
 * TC: O(n^2), SC: O(n)
 */

function lengthOfLIS(nums: number[]): number {
  const n = nums.length;
  const dp = new Array(n).fill(1); // In Python => [1] * n

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        dp[i] = Math.max(dp[j] + 1, dp[i]);
      }
    }
  }
  return Math.max(...dp); // 숫자 배열을 펼쳐 여러 숫자를 넘겨줘야 함
}
