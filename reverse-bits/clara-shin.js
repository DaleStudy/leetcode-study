/**
 * 비트 반전 문제(32비트 무부호 정수, 32 bits unsigned integer)
 * 비트 반전: 32비트 전체를 뒤집는 것(왼쪽과 오른쪽을 바꾸는 것)
 *
 * 접근 방법:
 * 32비트 정수의 각 비트를 오른쪽에서 왼쪽으로 순회하며 확인
 * 각 비트를 왼쪽에서 오른쪽으로 반대로 위치시킴
 * 각 위치에 따라 결과값에 더함
 *
 * 시간복잡도: O(1)
 * 공간복잡도: O(1)
 */
/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  let result = 0;

  for (let i = 0; i < 32; i++) {
    // 결과에 현재 비트를 추가 (비트 OR 연산)
    // 결과를 왼쪽으로 시프트한 후, n의 최하위 비트가 1이면 결과에 1을 더함
    result = (result << 1) | (n & 1);

    // n을 오른쪽으로 시프트
    n >>>= 1;
  }

  // 부호 없는 정수로 변환
  return result >>> 0;
};
