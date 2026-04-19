/*
dp 배열 생성, top-left에서 bottom-right로 이동하며 위 값, 왼쪽 값을 더하며 dp를 업데이트, 마지막 원소를 리턴한다

시간복잡도 : O(m * n)
*/

const dx = [0, 1]
const dy = [1, 0]

function uniquePaths(m: number, n: number): number {
  const dp = Array.from({ length: m }, () => new Array(n).fill(1))

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    }
  }

  return dp[m - 1][n - 1]
}
