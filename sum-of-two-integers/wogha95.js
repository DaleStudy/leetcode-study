/**
 * TC: O(Bit)
 * 올림 비트가 0일때까지 while을 실행하게된다.
 *
 * SC: O(log(max(a, b)))
 *
 * Bit: 2진수 a 와 b 중 비트 길이가 긴 것의 비트 길이
 */

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function (a, b) {
  while (b !== 0) {
    const carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
  }

  return a;
};
