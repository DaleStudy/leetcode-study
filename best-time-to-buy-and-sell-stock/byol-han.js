/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minPrice = Infinity;
  let maxProfit = 0;

  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < minPrice) {
      minPrice = prices[i]; // 지금까지 가장 싼 날
    } else if (prices[i] - minPrice > maxProfit) {
      maxProfit = prices[i] - minPrice; // 현재 이익이 최대 이익보다 클 때 maxProfit 갱신
    }
  }

  return maxProfit;
};
