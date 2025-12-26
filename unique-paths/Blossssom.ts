/**
 * @param m - grid row length
 * @param n - grid col length
 * @returns - 오른쪽 아래 모서리에 도착할 수 있는 경로의 수
 * @description
 * - [0, 0] 시작
 * - 아래쪽 혹은 오른쪽으로만 이동 가능
 * - dfs인줄 알았는데 visit도 필요 없고 결국 dp.
 *
 * - 풀이 1. 각 지점에 도달할 수 있는 경우는 이전 idx의 경우의 수들 (x - 1, y - 1)의 합이다.
 * - 따라서 이전 idx의 값들을 누적해가며 가장 마지막인 도착점의 누적 값이 결과.
 *
 * - 풀이 2. 풀이 1과 방식은 같지만 1차원 배열을 덮어 씌워가며 공간 복잡도를 줄임
 */

// function uniquePaths(m: number, n: number): number {
//   const dp = Array.from({ length: m }, () =>
//     Array.from({ length: n }, () => 1)
//   );

//   for (let i = 1; i < m; i++) {
//     for (let j = 1; j < n; j++) {
//       dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
//       console.log(dp);
//     }
//   }

//   return dp[m - 1][n - 1];
// }

function uniquePaths(m: number, n: number): number {
  const dp = Array.from({ length: n }, () => 1);

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[j] += dp[j - 1];
    }
  }
  return dp[n - 1];
}

const m = 3;
const n = 7;
uniquePaths(m, n);


