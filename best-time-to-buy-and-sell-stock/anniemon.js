/**
 * 시간 복잡도: prices.length만큼 순회하므로 O(n)
 * 공간 복잡도: 상수 크기의 변수만 사용하므로 O(1)
 */
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let maxProfit = 0;
  let min = prices[0];

  for (let i = 0; i < prices.length; i++) {
      maxProfit = Math.max(maxProfit, prices[i] - min);
      min = Math.min(min, prices[i]);
  }
  return maxProfit;
};
