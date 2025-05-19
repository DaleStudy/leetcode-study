/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  // 가장 작은 수
  let minNum = prices[0];
  // 차이 값
  let maxProfit = 0;
  for (let i = 1; i < prices.length; i++) {
    minNum = Math.min(minNum, prices[i - 1]); // 이전꺼 중 가장 작은 수
    maxProfit = Math.max(maxProfit, prices[i] - minNum);
  }
  return maxProfit;
};
