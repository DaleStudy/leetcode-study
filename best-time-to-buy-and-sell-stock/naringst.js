/**
 * @param {number[]} prices
 * @return {number}
 */

/**
 * Runtime: 73ms, Memory: 59.38MB
 * n = prices.length
 * Time complexity: O(n)
 * Space complexity: O(1)
 *
 */

var maxProfit = function (prices) {
  let minPrice = prices[0];
  let maxPrice = prices[0];
  let answer = 0;

  for (let i = 1; i < prices.length; i++) {
    answer = Math.max(answer, maxPrice - minPrice);

    // 가장 뒤쪽 값이 max일 때
    if (maxPrice < prices[i]) {
      maxPrice = prices[i];
      answer = Math.max(answer, maxPrice - minPrice);
      continue;
    }
    // 가장 뒷쪽 값이 min일 때
    if (minPrice > prices[i]) {
      minPrice = prices[i];
      maxPrice = prices[i];
    }
  }
  return answer;
};
