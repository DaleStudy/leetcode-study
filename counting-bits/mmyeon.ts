/**
 *
 * 접근 방법 :
 *  - 2진수 사이의 1의 개수가 이전 값의 결과에 의존하는 규칙이 있어서 dp로 진행
 *  - 2로 나눠서 짝수인지 홀수인지 판별
 *  - 짝수인 경우, 2로 나눈 몫의 값(이전 값)을 재활용하고, 홀수인 경우 내림처리 해서 이전 값에 1 더해주기
 *
 *
 * 시간복잡도 :
 *  - 숫자 길이만큼 순회하는 for문 - O(n)
 *
 * 공간복잡도 :
 *  - 숫자 길이와 동일한 길이의 배열 저장하므로 O(n)
 *
 *
 */
function countBits(n: number): number[] {
  if (n === 0) return [0];

  let answer = [0, 1];

  for (let i = 2; i <= n; i++) {
    // 짝수인지 홀수인지 체크
    if (i % 2 === 0) {
      answer[i] = answer[i / 2];
    } else {
      answer[i] = answer[Math.floor(i / 2)] + 1;
    }
  }
  return answer;
}
