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

// 2번째 시도
// 1. 재귀 접근의 경우 메모리와 콜스택 과부하가 있을 수 있음.
// 2. 모든 경우의 수가 아닌 바로 직전 단계까지의 합산 값만 있어도 결과 도출이 가능하다.

function climbStairs(n: number): number {
  if (n === 1) return 1;
  if (n === 2) return 2;

  let prev2 = 1; // n-2번째
  let prev1 = 2; // n-1번째
  let cur = 0;

  for (let i = 3; i <= n; i++) {
    cur = prev2 + prev1;
    prev2 = prev1;
    prev1 = cur;
  }

  return cur;
}
