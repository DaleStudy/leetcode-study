function climbStairs(n: number): number {
  let result = 0;
  let step1 = 1;
  let step2 = 0;

  for (let i = 0; i < n; i++) {
    result = step1 + step2;
    step2 = step1;
    step1 = result;
  }
  return result;
}
