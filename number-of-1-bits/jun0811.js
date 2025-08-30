/**
 * @param {number} n
 * @return {number}
 */

// 1주차에 풀이 후 제출..

var hammingWeight = function (n) {
  let res = 0;
  while (n > 0) {
    res += n & 1;
    n = n >> 1; // 나누기 2
  }
  return res;
};
