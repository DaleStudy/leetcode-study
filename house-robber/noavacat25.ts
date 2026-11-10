/*
시간 복잡도: O(n)
공간 복잡도: O(1)
풀이 알고리즘: DP(Dynamic Programming) 이용 (Space-Optimised DP)

해설: dp[i] = max(dp[i-2] + nums[i], dp[i-1]) 로 점화식을 세울 수 있다.
dp[i-2]와 dp[i-1]만 있으면 dp[i]를 구할 수 있으므로, dp 배열을 만들지 않고 두 개의 변수(secondLast, last)만으로도 구현 가능하다.

점화식: dp[i] = max(dp[i−2] + nums[i], dp[i−1])
Dynamic Programming 기법에 의해, secondLast와 last를 다음 Iteration에서 재사용할 수 있도록 저장하여 공간 최적화(Space-Optimisation)를 활용할 수 있다.
*/
const rob = (nums: number[]): number => {
  const n = nums.length

  if (n === 0) return 0
  if (n === 1) return nums[0]

  let secondLast = 0
  let last = nums[0]

  let result = -1

  for (let i = 1; i < n; i++) {
    result = Math.max(nums[i] + secondLast, last)
    secondLast = last
    last = result
  }

  return result
}
