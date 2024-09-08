/**
 * TC: O(N)
 * SC: O(1)
 */

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let maximumProfit = 0;
  let minimumPrice = prices[0];

  for (const price of prices) {
    // 매일 (그날까지의) 최소 구매가를 기록합니다.
    minimumPrice = Math.min(minimumPrice, price);
    // 최대 이익을 갱신합니다.
    maximumProfit = Math.max(maximumProfit, price - minimumPrice);
  }

  return maximumProfit;
};
