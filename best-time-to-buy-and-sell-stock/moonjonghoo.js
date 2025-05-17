/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minPrices = Infinity;
  let profit = 0;
  for (price of prices) {
    minPrices = Math.min(price, minPrices);
    profit = Math.max(profit, price - minPrices);
  }
  return profit;
};

var maxProfit = function (prices) {
  let maxProfit = 0;
  let currentProfit = 0;
  for (let i = 1; i < prices.length; i++) {
    let diff = prices[i] - prices[i - 1];
    currentProfit = Math.max(0, currentProfit + diff);
    maxProfit = Math.max(maxProfit, currentProfit);
  }
  return maxProfit;
};
