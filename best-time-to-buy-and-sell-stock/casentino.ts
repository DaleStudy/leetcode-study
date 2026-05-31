function maxProfit(prices: number[]): number {
  const dp = new Array(prices.length).fill(0);
  dp[0] = 0;
  let maxProfit = 0;
  for (let i = 1; i < prices.length; i++) {
    dp[i] = Math.max(prices[i] - prices[i - 1], prices[i] - prices[i - 1] + dp[i - 1]);

    maxProfit = Math.max(dp[i], maxProfit);
  }
  return maxProfit;
}
