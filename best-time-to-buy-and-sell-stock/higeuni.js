/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let answer = 0
  let leftMin = prices[0]

  for(let i = 1; i < prices.length; ++i) {
      answer = Math.max(answer, prices[i] - leftMin);
      leftMin = Math.min(prices[i], leftMin);
  }

  return answer;
};

