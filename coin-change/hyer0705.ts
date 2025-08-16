function coinChange(coins: number[], amount: number): number {
  // dp[i] = i 금액을 만드는 데 필요한 최소 동전의 갯수...
  const dp: number[] = Array(amount + 1).fill(Infinity);
  dp[0] = 0;

  for (let i = 1; i <= amount; i++) {
    let min = Infinity;
    for (const coin of coins) {
      if (i >= coin) {
        min = Math.min(dp[i - coin] + 1, min);
      }
    }
    dp[i] = min;
  }

  return Number.isFinite(dp[amount]) ? dp[amount] : -1;
}
