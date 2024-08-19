/**
 * @description
 * time complexity: O(logN)
 * space complexity: O(1)
 * approach/strategy:
 * 1. decimal to binary
 */

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let answer = 0;

  while (n > 0) {
    answer += n % 2;
    n = Math.floor(n / 2);
  }

  return answer;
};
