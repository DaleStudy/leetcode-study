/**
 * 복잡도 분석:
 * - 시간: O(n) - 3부터 n까지 한 번씩 순회
 * - 공간: O(1) - prev1, prev2 두 변수만 사용
 */

/**
 * @param {number} n
 * @return {number}
 */
const climbStairs = (n) => {
  // 기본 케이스: 1칸이면 1가지, 2칸이면 2가지
  if (n <= 2) return n;

  /**
   * 아이디어:
   * n번째 계단에 도달하는 방법 =
   *   1) n-1번째 계단에서 1칸 오르기
   *   2) n-2번째 계단에서 2칸 오르기
   *
   * 즉, f(n) = f(n-1) + f(n-2) 피보나치 수열과 동일
   *
   * 재귀로 풀면 중복 계산이 많아서 비효율적
   * → 이전 두 값만 기억하면서 반복문으로 해결
   */

  let prev2 = 1; // f(1) = 1
  let prev1 = 2; // f(2) = 2

  // 3부터 n까지 차례대로 계산
  for (let i = 3; i <= n; i++) {
    const current = prev1 + prev2; // 현재 = 이전 + 이전의 이전
    prev2 = prev1; // 값들을 한 칸씩 앞으로 이동
    prev1 = current;
  }

  return prev1;
};
