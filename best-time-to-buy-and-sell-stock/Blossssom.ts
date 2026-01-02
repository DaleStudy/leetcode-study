function maxProfit(prices: number[]): number {
  let min = prices[0];
  let max = 0;

  for (let i = 0; i < prices.length; i++) {
    min = Math.min(min, prices[i]);
    max = Math.max(max, prices[i] - min);
  }

  return max;
}

const prices = [3, 3, 5, 0, 0, 3, 1, 4];
maxProfit(prices);


