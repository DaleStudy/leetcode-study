function climbStairs(n: number): number {
  if (n <= 2) return n;

  let dp1 = 1;
  let dp2 = 2;

  for (let i = 3; i <= n; i++) {
    let sum = dp1 + dp2;
    dp1 = dp2;
    dp2 = sum;
  }

  return dp2;
}

climbStairs(2); // 2
climbStairs(3); // 3
climbStairs(24); // 75025
climbStairs(45); // 1836311903
