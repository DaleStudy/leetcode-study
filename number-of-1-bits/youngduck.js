/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  // 이진수 변환함수 시간복잡도: O(1)
  const bin = n.toString(2);

  // replace, replaceAll 시간복잡도: O(n)
  const result = bin.replaceAll('0', '').length;

  // 시간복잡도: O(n), 공간복잡도: O(1)

  return result;
};
