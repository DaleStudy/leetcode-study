/**
 * @param {number} n - a positive integer
 * @return {number} - reversed bits
 */
var reverseBits = function (n) {
  let result = 0;
  for (let i = 0; i < 32; i++) {
    result <<= 1; // 왼쪽으로 1비트 이동
    result |= n & 1; // 마지막 비트 추출해서 결과에 추가
    n >>>= 1; // 부호 없는 우측 시프트 (>>>)
  }
  return result >>> 0; // unsigned 32비트 정수로 변환
};
