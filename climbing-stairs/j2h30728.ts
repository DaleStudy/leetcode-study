function climbStairs(n: number): number {
  if (n === 0 || n === 1) {
    return 1;
  }

  const memo: number[] = [];
  memo[0] = memo[1] = 1;

  for (let i = 2; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2];
  }

  return memo[n];
}
