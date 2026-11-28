// 시간 복잡도: O(log n)
// 공간 복잡도: O(1)

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let cnt = 0;
  while (n > 0) {
    const r = n % 2;
    if (r == 1) cnt++;
    n = Math.floor(n / 2);
  }
  return cnt;
};
