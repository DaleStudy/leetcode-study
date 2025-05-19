/**
 * 시간 복잡도 O(n)
 * 공간 복잡도 O(1)
 *
 * 그리디 알고리즘
 * 현재까지의 최저 가격을 기억하고, 그 가격에 샀을 때의 이익을 계속 계산하여 최대 이익을 구함
 */

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minPrice = prices[0]; // 최저 가격 초기화 (첫 날 가격)
  let maxProfit = 0; // 최대 이익 초기화 (아직 이익 없음)

  // 두 번째 날부터
  for (let i = 1; i < prices.length; i++) {
    minPrice = Math.min(minPrice, prices[i]); // 최저 가격 갱신
    maxProfit = Math.max(maxProfit, prices[i] - minPrice); // 최대 이익 갱신
  }

  return maxProfit;
};
