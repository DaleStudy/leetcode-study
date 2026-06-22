/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let cnt = 1;
  while (n >= 2) {
    const r = n % 2;
    n = Math.floor(n / 2);
    if (r === 1) cnt++;
  }
  return cnt;
};
