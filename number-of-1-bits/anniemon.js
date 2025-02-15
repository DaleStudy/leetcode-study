/**
 * 시간 복잡도: n을 나누는 횟수는 n의 비트 수에 비례하므로, O(log n)
 * 공간 복잡도: 비트 문자열의 길이도 n의 비트 수에 비례하므로, O(log n)
 */
/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
  let bi = '';
  while(n / 2 > 0) {
      bi += (n % 2).toString();
      n = Math.floor(n / 2)
  }
  return (bi.match(/1/g) || []).length
};
