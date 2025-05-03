function coinChange(coins: number[], amount: number): number {
  const dp = [0, ...new Array(amount).fill(amount + 1)];
  for (let i = 0; i <= amount; i++) {
    for (const coin of coins) {
      if (coin <= i) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    }
  }
  return dp[amount] < amount + 1 ? dp[amount] : -1;
}
