/*
 * TC: O(amount * coins.length)
 * SC: O(amount)
 * */
function coinChange(coins: number[], amount: number): number {
  if (amount === 0) {
    return 0;
  }

  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;

  for (let i = 1; i <= amount; i++) {
    coins.forEach((coin) => {
      if (coin <= i) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    });
  }

  return dp[amount] === Infinity ? -1 : dp[amount];
}
