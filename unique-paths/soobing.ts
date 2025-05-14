/**
 * 문제 설명
 * - m행과 n열의 그래프에서 오른쪽 아래에 도달할 수 있는 방법의 가짓수
 * - 아래, 오른쪽으로만 이동 가능
 *
 * 아이디어
 * 1) DP
 * - 첫번째 행, 첫번째 열을 제외하고나서는 (m - 1)번 아래 + (n - 1)번 오른쪽을 더한 값이 현재 위치에 올 수 있는 방법임.
 * - 전부 거친다음 가장 오른쪽 아래의 값을 반환하면 정답
 * 2) 조합 -> factorial의 경우 Maximum call stack size exceed 발생
 * - 아래로 이동 가능한 수(m-1), 오른쪽으로 이동 가능한 수 (n-1)의 조합
 * - (m + n - 2)! / (m - 1)! * (n - 1)!
 */
function uniquePaths(m: number, n: number): number {
  const dp = Array(m).fill(Array(n).fill(1));

  for (let r = 1; r < m; r++) {
    for (let c = 1; c < n; c++) {
      dp[r][c] = dp[r - 1][c] + dp[r][c - 1];
    }
  }

  return dp[m - 1][n - 1];
}

/**
 * factorial 풀이 -> 에러발생
 *
function uniquePaths(m: number, n: number): number {
  function factorial(n: number) {
    if (n === 1) return 1;

    return n * factorial(n - 1);
  }

  return factorial(m + n - 2)! / (factorial(m - 1) * factorial(n - 1));
}
*/
