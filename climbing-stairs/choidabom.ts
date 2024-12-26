/**
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 *
 * 접근: 1번째 계단을 오르는 방법은 1가지, 2번째 계단을 오르는 방법은 2가지 (계단은 한 번에 1칸 또는 2칸씩만 오를 수 있다.)
 * n 번째 계단에 오르는 방법은 '한 칸 전 계단(n-1)에서 오르는 1칸 올라오는 방법' + '두 칸 전 계단(n-2)에서 2칸 올라오는 방법'
 */

function climbStairs(n: number): number {
  let stairs = [1, 2];

  for (let i = 2; i < n; i++) {
    stairs[i] = stairs[i - 1] + stairs[i - 2];
  }

  return stairs[n - 1];
}

function climbStairs(n: number): number {
  let dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i < n + 1; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}

console.log(climbStairs(5));
