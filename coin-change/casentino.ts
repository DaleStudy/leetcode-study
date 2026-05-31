function coinChange(coins: number[], amount: number): number {
  const dp = new Array(amount + 1).fill(amount);
  dp[0] = 0;
  for (let i = 1; i <= amount; i++) {
    for (let j = 0; j < coins.length; j++) {
      if (i - coins[j] >= 0) {
        dp[i] = Math.min(dp[i - coins[j]] + 1, dp[i]);
      }
    }
  }
  return dp[amount] === Number.POSITIVE_INFINITY ? -1 : dp[amount];
}
