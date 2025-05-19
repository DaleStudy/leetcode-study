/**
 * https://leetcode.com/problems/unique-paths/
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
  // 2차원 배열 생성 (m행 n열), 모든 값을 1로 초기화
  const dp = Array.from({ length: m }, () => Array(n).fill(1));

  // (1,1)부터 시작해서 경로 수 계산
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }

  // 오른쪽 아래 모서리의 값이 정답
  return dp[m - 1][n - 1];
};
