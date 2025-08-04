// 1번풀이 (hashMap)
function climbStairs1(n: number): number {
  const dp: Record<number, number> = {
    1: 1,
    2: 2,
  };

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
};

// 2번풀이 (배열)
function climbStairs2(n: number): number {
  const dp = [0, 1, 2]; // dp[1] = 1, dp[2] = 2

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
};

// 3번풀이
// 불필요한 배열 전체 저장을 제거하고, 필요한 값만 2개만 유지
function climbStairs(n: number): number {
  if (n <= 2) return n;

  let prev1 = 1; // dp[i - 2]
  let prev2 = 2; // dp[i - 1]

  for (let i = 3; i <= n; i++) {
    const current = prev1 + prev2;
    prev1 = prev2;
    prev2 = current;
  }

  return prev2;
};

