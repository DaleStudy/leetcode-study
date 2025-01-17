// Time complexity: O(n)
// Space complexity: O(1)

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let answer = 0;
  let minValue = Number.MAX_SAFE_INTEGER;

  for (const price of prices) {
    minValue = Math.min(minValue, price);
    answer = Math.max(answer, price - minValue);
  }

  return answer;
};
