// Time Complexity: O(n), where n is the length of the prices array
// Space Complexity: O(1)

function maxProfit(prices: number[]): number {
  // input: an array prices, prices[i] = the stock price of ith day
  // output: the maximum profit || 0

  // prices = [7, 1, 5, 3, 6, 4]
  // buy = 1, sell = 6, profit = 6 -1 = 5

  let minBuy = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    minBuy = Math.min(prices[i], minBuy);
    maxProfit = Math.max(prices[i] - minBuy, maxProfit);
  }

  return maxProfit;
}

