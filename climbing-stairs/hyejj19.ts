function climbStairs(n: number, memo = {}): number {
  // 재귀 종료조건
  if (n === 1) return 1;
  if (n === 2) return 2;

  // 값이 메모에 존재하면 해당 값을 리턴
  if (memo[n] !== undefined) return memo[n];

  // 아니라면 계산 후 메모이징
  memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo);

  return memo[n];
}
