// TC: O(n)
// SC: O(n)
function countBits(n: number): number[] {
  const dp: number[] = [];
  dp[0] = 0;

  for (let i = 0; i <= n; i++) {
    dp[i] = dp[i >> 1] + (i & 1);
  }

  // The number of 1s in the quotient (i >> 1) + number of 1s in the remainder (i & 1)
  // dp[i >> 1]: number of 1's in Math.floor(i / 2)
  // i & 1: 1 if i is odd, 0 if even

  return dp;
}

