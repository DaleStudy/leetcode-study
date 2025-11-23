function climbStairs(n: number): number {
  const memo = new Array(n + 1).fill(-1);
  function climb(stair: number) {
    if (stair === 0) {
      return 1;
    }
    if (stair < 0) {
      return 0;
    }
    if (memo[stair] !== -1) {
      return memo[stair];
    }
    memo[stair] = climb(stair - 1) + climb(stair - 2);
    return memo[stair];
  }
  return climb(n);
}
