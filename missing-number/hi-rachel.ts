/**
 * https://leetcode.com/problems/missing-number/
 *
 * 문제 설명:
 *  - 0부터 n까지의 숫자 중 하나가 빠진 길이 n의 배열 nums가 주어집니다.
 *  - 이 때, 누락된 숫자 하나를 찾아 반환하세요.
 *
 *  조건:
 *  - nums.length == n
 *  - nums의 요소는 고유하며 [0, n] 범위의 정수를 포함합니다.
 *
 *  풀이 아이디어:
 *  - 0부터 n까지의 총합을 공식으로 계산한 후, 실제 배열의 총합을 뺍니다.
 *    0부터 n까지의 합 공식:
 *    0 + 1 + 2 + ... + n = n(n + 1)/2
 *  - 빠진 숫자 = 기대 총합 - 실제 총합
 *
 *  TC: O(n)
 *   - 배열 순회로 실제 합을 구하는 데 O(n)
 *
 *  SC: O(1)
 *   - 추가 공간 없이 상수 변수만 사용
 */

function missingNumber(nums: number[]): number {
  const expectedSum = Math.floor((nums.length * (nums.length + 1)) / 2);
  const actualSum = nums.reduce((acc, cur) => acc + cur);
  return expectedSum - actualSum;
}
