/**
 *
 * 접근 방법 : dp 사용
 *  - 3번째 스텝부터 이전 값 2개의 합으로 구할 수 있다.
 *  - 반복문을 통해서, 저장해놓은 이전값의 합으로 현재값 구하기
 *  - 다음값 구하기 위해서, 이전값을 이전이전값으로, 현재값을 이전값으로 업데이트해주기
 *  - 현재값 리턴하기
 *
 * 시간복잡도 :
 *  - 0부터 주어진 n번째스텝까지 순회해야 하므로 O(n)
 *
 * 공간복잡도 :
 *  - 이전값 저장하기 위해서 변수 2개가 쓰이므로 O(1)
 *
 */

function climbStairs(n: number): number {
  if (n <= 2) return n;

  let prevPrevSteps = 1;
  let prevSteps = 2;

  for (let i = 3; i <= n; i++) {
    const currentSteps = prevPrevSteps + prevSteps;
    prevPrevSteps = prevSteps;
    prevSteps = currentSteps;
  }

  return prevSteps;
}
