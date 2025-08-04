/**
 * https://leetcode.com/problems/longest-increasing-subsequence/
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
  if (nums.length === 0) return 0;

  const dp = new Array(nums.length).fill(1); // 최소 길이는 1 (자기 자신만 포함)

  for (let i = 1; i < nums.length; i++) {
    // 현재 숫자 이전의 숫자들과 비교
    for (let j = 0; j < i; j++) {
      // 증가하는 순서인지 확인
      if (nums[i] > nums[j]) {
        // 증가하는 subsequence가 발견되면 길이 갱신
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return Math.max(...dp);
};
