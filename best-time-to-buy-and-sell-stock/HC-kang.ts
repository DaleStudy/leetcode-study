// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// T.C: O(N)
// S.C: O(1)
function maxProfit(prices: number[]): number {
  let min = prices[0];
  let max = prices[0];
  let candidate = prices[0];

  for (let i = 1; i < prices.length; i++) {
    if (prices[i] < candidate) {
      candidate = prices[i];
    } else if (prices[i] - candidate > max - min) {
      min = candidate;
      max = prices[i];
    }
  }

  return max - min;
}
