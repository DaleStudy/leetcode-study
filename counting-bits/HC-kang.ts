// T.C: O(n)
// S.C: O(n)
function countBits(n: number): number[] {
  // T.C: O(1)
  // S.C: O(1)
  function countBit(num: number): number {
    num = num - ((num >>> 1) & 0x55555555);
    num = (num & 0x33333333) + ((num >>> 2) & 0x33333333);
    num = (num + (num >>> 4)) & 0x0f0f0f0f;
    num = num + (num >>> 8);
    num = num + (num >>> 16);
    return num & 0x3f;
  }

  return new Array(n + 1).fill(0).map((_, i) => countBit(i));
}

// T.C: O(n)
// S.C: O(n)
function countBits(n: number): number[] {
  const dp = new Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    dp[i] = dp[i >> 1] + (i & 1);
  }
  return dp;
}
