/**
dp 배열을 만들고 각 원소 순서에서 최대의 값을 계산, 리턴한다

시간복잡도
O(N) : 단일 순회

공간복잡도
O(N) : dp 배열
 */

function rob(nums: number[]): number {
  const dp = []

  for (let i = 0; i < nums.length; i++) {
    if (i < 1) {
      dp[i] = nums[i]
    } else if (i < 2) {
      dp[i] = Math.max(dp[i - 1], nums[i])
    } else {
      dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1])
    }
  }

  return dp.at(-1)
}
