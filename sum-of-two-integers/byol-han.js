/**
 * https://leetcode.com/problems/sum-of-two-integers/submissions/1649575939/
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function (a, b) {
  while (b !== 0) {
    // a와 b의 합에서 자리올림(carry)을 제외한 값 계산 (XOR 연산)
    let sum = a ^ b;

    // 자리올림(carry)을 계산 (AND 연산 후 왼쪽으로 한 비트 이동)
    let carry = (a & b) << 1;

    // 새로운 a는 sum, 새로운 b는 carry가 됨
    a = sum;
    b = carry;
  }

  // carry가 0이 되면 더할 게 없으므로 최종 결과 a 반환
  return a;
};
