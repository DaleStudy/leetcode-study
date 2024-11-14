/**
 * TC: O(1)
 * n 숫자를 32자리 2진수로 변환하고 배열로 변경했을때 최대 길이가 32이므로 상수 복잡도를 갖는다.
 *
 * SC: O(1)
 */

/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  const result = n.toString(2).padStart(32, "0").split("").reverse().join("");
  return parseInt(result, 2);
};
