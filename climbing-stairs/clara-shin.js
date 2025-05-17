/**
 * 계단을 오르는 방법은 몇 가지?
 * 총 n개의 계단
 * 한 번에 1계단 또는 2계단을 오를 수 있다
 * 계단 꼭대기에 도달하는 서로 다른 방법의 수를 구해보자
 *
 * ✨동적 프로그래밍(Dynamic Programming)✨
 * 재귀 접근법
 * 메모이제이션을 사용한 재귀
 * 동적 프로그래밍(바텀업)
 * 피보나치 수열: n번째 계단에 도달하는 방법의 수는 (n-1)번째와 (n-2)번째 계단에 도달하는 방법의 수의 합과 같음
 */

/**
 * @param {number} n
 * @return {number}
 */
function climbStairs(n) {
  // 예외 처리: n이 1 이하인 경우 빨리 1 리턴하고 탈출
  if (n <= 1) {
    return 1;
  }

  // 피보나치 수열 계산을 위한 변수
  let first = 1; // f(0) = 1
  let second = 1; // f(1) = 1
  let result;

  // 피보나치 수열 계산
  for (let i = 2; i <= n; i++) {
    result = first + second;
    first = second;
    second = result;
  }

  return result;
}

// 시간 복잡도: O(n) - n번의 반복문을 수행
// 공간 복잡도: O(1) - 상수 개의 변수만 사용
// 제약조건이 n은 최대 45까지니까 피보나치 접근법이 좋은 선택인 듯
