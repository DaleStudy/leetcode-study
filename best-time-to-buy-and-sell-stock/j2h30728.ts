function maxProfit(prices: number[]): number {
  let min = Infinity;
  let result = 0;

  for (const price of prices) {
    min = Math.min(price, min);
    result = Math.max(result, price - min);
  }

  return result;
}
