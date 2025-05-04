function maxProfit(prices: number[]): number {
  let minPrice = Number.MAX_SAFE_INTEGER;
  let maxProfit = 0;

  for (let i = 0; i < prices.length; i++) {
    const currentPrice = prices[i];

    if (currentPrice < minPrice) {
      minPrice = currentPrice;
    } else {
      const profit = currentPrice - minPrice;
      maxProfit = Math.max(maxProfit, profit);
    }
  }

  return maxProfit;
};

maxProfit([7, 1, 5, 3, 6, 4]); // Output: 5
maxProfit([7, 6, 4, 3, 1]); // Output: 0
maxProfit([2, 4, 1]); // Output: 2
maxProfit([1, 2]); // Output: 1
maxProfit([2, 1]); // Output: 0
maxProfit([1, 2, 3, 4, 5]); // Output: 4
