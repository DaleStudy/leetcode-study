/**
 * 문제 유형
 * - Array, DP
 *
 * 문제 설명
 * - 배열에서 "연속된" 부분 배열의 합 중 가장 큰 값을 구하기
 *
 * 아이디어
 * 1) Bottom-Up 방식
 * - dp에는 앞에서부터 이어붙인 값이 큰지, 현재 값에서 다시 시작하는게 클지 비교하여 큰 값 저장 (현재 기준)
 * - maxSum은 전체 dp중 가장 큰 값을 저장
 */
function maxSubArray(nums: number[]): number {
  const dp = new Array(nums.length);
  dp[0] = nums[0];
  let maxSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
    maxSum = Math.max(maxSum, dp[i]);
  }
  return maxSum;
}
