function maxProfit(prices: number[]): number {
  let minPrice = Number.MAX_SAFE_INTEGER;
  let maxProfit = 0;

  for (let p of prices) {
    if (minPrice >= p) {
      minPrice = p;
      continue;
    } else {
      let profit = p - minPrice;
      if (profit > maxProfit) maxProfit = profit;
    }
  }
  return maxProfit;
}

function maxProfit(prices: number[]): number {
  let minPrice = Infinity;
  let maxProfit = 0;

  for (let p of prices) {
    minPrice = Math.min(minPrice, p);
    maxProfit = Math.max(maxProfit, p - minPrice);
  }
  return maxProfit;
}
