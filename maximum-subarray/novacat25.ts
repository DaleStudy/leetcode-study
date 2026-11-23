/*
시간 복잡도: O(n)
공간 복잡도: O(1)
풀이 기법: Dynamic Programming + Space Optimisation(Kadane's Algorithm)
dp[i] = max(dp[i-1] + nums[i], nums[i])의 점화식을 활용할 수 있다.
*/
const maxSubArray = (nums: number[]): number => {
  const n = nums.length
  if (n === 1) return nums[0]

  let maxEnding = nums[0]
  let result = nums[0]

  for (let i = 1; i < nums.length; i++) {
    const currentNum = nums[i]
    maxEnding = Math.max(currentNum + maxEnding, currentNum)
    result = Math.max(result, maxEnding)
  }

  return result
}
