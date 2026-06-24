/**
 * 인접하지 않은 노드들의 합 중 가장 큰 값을 반환하는 문제.
 *
 * 동적 계획법(DP)으로 해결한다.
 * 각 노드를 포함했을 때 얻을 수 있는 최댓값을 dp 배열에 저장해두고,
 * 마지막에 그 최댓값을 반환한다.
 *
 * 시간 복잡도 O(n): 노드를 한 번씩만 순회한다.
 * 공간 복잡도 O(n): 길이 n의 dp 배열을 사용한다.
 */

function rob(nums: number[]): number {
  const dp = new Array(nums.length).fill(0);

  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  dp[0] = nums[0];
  dp[1] = nums[1];
  dp[2] = nums[0] + nums[2];

  for (let i = 3; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 2], dp[i - 3]) + nums[i];
  }

  return Math.max(...dp);
}
