/**
 * n개의 서로 다른 숫자가 들어있는 배열에서, 0부터 n까지의 범위 중 빠진 숫자 하나를 찾는 문제
 * 배열의 길이가 n이면, 실제로는 0부터 n까지 총 (n+1)개의 숫자 중 하나가 빠져있음
 *
 * 접근방법: XOR 비트 연산
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 *
 * XOR의 성질:
 * - a ^ a = 0 (같은 수끼리 XOR하면 0)
 * - a ^ 0 = a (어떤 수든 0과 XOR하면 자기 자신)
 * - XOR은 교환법칙과 결합법칙이 성립
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  let result = nums.length; // n으로 초기화

  // 인덱스 i와 nums[i]를 모두 XOR
  // 결국 빠진 숫자만 홀수 번 나타나서 결과로 남음
  for (let i = 0; i < nums.length; i++) {
    result ^= i ^ nums[i];
  }

  return result;
};
