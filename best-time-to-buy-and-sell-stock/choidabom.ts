/**
 * Runtime: 6ms, Memory: 62.30MB
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

function maxProfit(prices: number[]): number {
  let buyingPrice = prices[0];
  let profit = 0;

  for (const price of prices) {
    buyingPrice = Math.min(price, buyingPrice);
    profit = Math.max(profit, price - buyingPrice);
  }

  return profit;
}

maxProfit([7, 1, 5, 3, 6, 4]);
