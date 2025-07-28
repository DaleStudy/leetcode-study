/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let res = 0;
  while (n > 0) {
    res += n & 1;
    n = n >> 1; // 나누기 2
  }
  return res;
};
