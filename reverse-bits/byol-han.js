/**
 * https://leetcode.com/problems/reverse-bits/
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  let result = 0;

  for (let i = 0; i < 32; i++) {
    // result를 왼쪽으로 1칸 밀기
    result <<= 1;

    // n의 마지막 비트를 result의 오른쪽 끝에 추가
    result |= n & 1;

    // n을 오른쪽으로 1칸 밀기
    n >>>= 1;
  }

  // >>> 0을 하면 부호 없는 32비트 정수로 반환됨
  return result >>> 0;
};
