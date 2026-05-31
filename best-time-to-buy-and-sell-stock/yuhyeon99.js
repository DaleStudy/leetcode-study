/**
 * @param {number[]} prices
 * @return {number}
 * i 번째 날에 주식의 가격을 prices[i]에 담고 있는 배열 prices가 주어졌을 때, 
 * 주식을 어떤 날에 한 번 사고 나중에 다른 날에 팔아서 달성 가능한 최대 이익을 구하라.
 * 
 */
var maxProfit = function(prices) {
  var maxProfit = 0;
  var minPrice = prices[0]

  for(let i = 0; i < prices.length; i ++) {
      let profit = prices[i] - minPrice;
      maxProfit = Math.max(profit, maxProfit);
      minPrice = Math.min(prices[i], minPrice);
  }

  return maxProfit;
};
