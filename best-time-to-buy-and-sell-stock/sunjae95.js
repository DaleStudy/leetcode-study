/**
 * @description
 * brainstorming:
 * brute force
 *
 * time complexity: O(n)
 * space complexity: O(1)
 */
var maxProfit = function (prices) {
  let answer, min, max;
  prices.forEach((price, i) => {
    if (i === 0) {
      min = price;
      max = price;
      answer = 0;
      return;
    }

    if (price > max) max = price;
    if (price < min) {
      min = price;
      max = price;
    }
    answer = Math.max(answer, max - min);
  });

  return answer;
};
