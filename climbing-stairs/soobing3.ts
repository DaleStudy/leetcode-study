function climbStairs(n: number): number {
  const memo = new Map<number, number>();
  
  function dp (n: number): number {
      if(n <= 1) return 1;
      if(memo.has(n)) return memo.get(n)!;

      const result = dp(n-1) + dp(n-2);
      memo.set(n, result);
      return result;
  }

  return dp(n);
};