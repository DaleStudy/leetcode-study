/**
 *
 * 문제 설명
 * - Longest Increasing Subsequence(LIS)
 * - 최장 증가 부분 수열
 *
 * 아이디어
 * 1) Brute Force
 * - 시간복잡도가 O(2^n)이라서 TLE(Time Limit Exceed) 발생
 * - 구현은 backtracking으로 해야함.
 *
 * 2) Dynamic Programming
 * - 시간복잡도: O(n^2)
 * - nums[i]의 이전 원소들 중 가장 긴 LIS에 1을 더해서 저장
 *
 * 3) Binary Search
 * - 시간 복잡도: (O(n log n))
 * - 다음 기회에 풀어봐야지..
 *
 */
function lengthOfLIS(nums: number[]): number {
  const dp = Array(nums.length).fill(1);

  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return Math.max(...dp);
}
