var countBits = function (n) {
  // Create array which has 0 element length of n
  const dp = new Array(n + 1).fill(0);
  let offset = 1;

  for (let i = 1; i <= n; i++) {
    if (offset * 2 === i) offset = i;
    dp[i] = 1 + dp[i - offset];
  }
  return dp;
};

/**
      0 -> 0000 -> dp[0] = 0
      1 -> 0001 -> dp[1] = 1 + dp[1-1] = 1
      2 -> 0010 -> dp[2] = 1 + dp[2-2] = 1
      3 -> 0011 -> dp[3] = 1 + dp[3-2] = 2
      4 -> 0100 -> dp[4] = 1 + dp[4-4] = 1
      5 -> 0101 -> dp[5] = 1 + dp[5-4] = 2
      6 -> 0110 -> dp[6] = 1 + dp[6-4] = 2
      7 -> 0111 -> dp[7] = 1 + dp[7-4] = 3
      8 -> 1000 -> dp[8] = 1 + dp[8-8] = 1
   */

// TC: O(n)
// SC: O(1)
