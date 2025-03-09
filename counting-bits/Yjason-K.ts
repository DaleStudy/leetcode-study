/**
 * 각 수의 비트의 개수를 계산하는 함수
 * @param {number} nums - 최대 수
 * @returns {number[]} - 각 수의 비트의 개수 배열
 *
 * 시간 복잡도: O(n)
 * - nums 만큼 반복하며, 각 수의 비트의 개수를 계산
 *
 * 공간 복잡도: O(n)
 * - dp 배열을 사용하여 O(n) 만큼 추가 공간이 필요
 */
function countBits(nums: number): number[] {
  // dp 배열을 생성하고, 모두 0으로 초기화합니다.
  const dp: number[] = new Array(nums + 1).fill(0);
  
  // 각 수에 대해, 비트의 개수를 계산합니다.
  for (let num = 1; num <= nums; num++) {
    // num을 2진수로 표현했을 때, 1의 개수는 2진수로 변환하여 문자열로 변환 후,
    // '1'이 포함된 문자열의 길이를 계산합니다.
    dp[num] = dp[Math.floor(num / 2)] + (num % 2);
  }
  
  return dp;
}

