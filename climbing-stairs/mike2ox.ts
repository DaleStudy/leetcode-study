/**
 * Source: https://leetcode.com/problems/climbing-stairs/description/
 * 요점: 동적 프로그래밍(DP) 접근법 - 피보나치 수열과 유사
 * 풀이 시간: 25분
 * 시간복잡도: O(n) - 마지막 결과값을 얻기위해 n번 반복
 * 공간복잡도: O(1) - 상수 공간만 사용
 */
function climbStairs(n: number): number {
  // 엣지 케이스를 사전에 처리(가지치기)
  if (n <= 0) return 0;
  if (n === 1) return 1;

  // 피보나치 수열 계산을 위한 변수
  let current = 1; // n=1일 때 방법의 수 (첫 번째 피보나치 수)
  let prev = 1; // n=0일 때 방법의 수 (초기값)
  let temp; // 교환을 위한 임시 변수

  // i는 2부터 시작하여 n까지 반복
  for (let i = 2; i <= n; i++) {
    // 현재 계단에 도달하는 방법의 수 = 이전 두 계단에 도달하는 방법의 수의 합
    temp = current;
    current = current + prev;
    prev = temp;
  }

  return current;
}
