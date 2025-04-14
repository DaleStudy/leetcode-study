/**
 * 숫자를 이진수로 변환하고 1의 개수를 세는 방법
 * Follow up: 이 함수가 여러 번 호출된다면?
 *
 * 단순히 모든 비트를 확인하는 방법: O(log n) 또는 32비트 정수의 경우 O(32)의 시간 복잡도
 * ➡️ Brian Kernighan의 알고리즘: O(k)
 * 1 비트의 수에 비례하여 실행 시간이 결정
 */

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let count = 0;

  while (n !== 0) {
    // n & (n-1)은 n의 마지막 1 비트를 제거
    n = n & (n - 1);
    count++;
  }

  return count;
};
