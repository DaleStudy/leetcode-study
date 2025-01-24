/**
 * @link https://leetcode.com/problems/unique-paths/
 *
 * 접근 방법 :
 *  - 시작부터 끝까지 누적된 경로의 수 찾아야 하니까 dp 사용
 *  - 첫 번째 행과, 첫 번째 열은 1로 고정이라서 dp 배열을 1로 초기화함
 *  - 점화식 : dp[x][y] = dp[x-1][y] + dp[x][y-1]
 *
 * 시간복잡도 : O(m * n)
 *  - m * n 행렬 크기만큼 순회하니까 O(m * n)
 *
 * 공간복잡도 : O(m * n)
 *  - 주어진 행렬 크기만큼 dp 배열에 값 저장하니까 O(m * n)
 */
function uniquePaths(m: number, n: number): number {
  // m x n 배열 선언
  const dp = Array.from({ length: m }, () => Array(n).fill(1));

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }

  return dp[m - 1][n - 1];
}

// 공간 복잡도를 O(n)으로 최적화하기 위해서 1차원 dp 배열 사용
function uniquePaths(m: number, n: number): number {
  const rows = Array(n).fill(1);

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      rows[j] = rows[j] + rows[j - 1];
    }
  }

  return rows[n - 1];
}
