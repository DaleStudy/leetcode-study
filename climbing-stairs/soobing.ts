/**
 * 문제 유형
 * - DP (피보나치)
 *
 * 문제 설명
 * - 계단을 올라가는 방법의 수를 구하기
 *
 * 아이디어
 * 1) 피보나치 수열 활용
 * - climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
 */
function climbStairsBottomUp(n: number): number {
  function fibonacci(n: number, memo = new Map<number, number>()) {
    if (n === 1) return 1;
    if (n === 2) return 2;

    if (memo.has(n)) return memo.get(n);
    const result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    memo.set(n, result);
    return result;
  }
  return fibonacci(n);
}

function climbStairsTopDown(n: number): number {
  const dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
}
