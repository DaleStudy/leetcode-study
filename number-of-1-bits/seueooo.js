/**
 * 정수 n의 이진수 표현에서 1의 개수를 반환
 * 시간복잡도 O(log n) - 매 반복마다 n이 절반으로 줄어듦
 * 공간복잡도 O(1)
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let count = 0;
  while (n > 0) {
    if (n % 2 === 1) count++;
    n = Math.floor(n / 2);
  }
  return count;
};
