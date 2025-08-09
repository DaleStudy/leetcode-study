/**
 * 문제 유형
 * - Binary (개념을 알고있는지), 기본적인 구현 문제
 *
 * 문제 설명
 * - 주어진 정수를 2진수로 변환했을때 1의 갯수를 구하는 문제
 *
 * 아이디어
 * 1) 나누기 2를 통해 2진수로 변환하고 1인 경우 갯수를 카운트한다.
 */
function hammingWeight(n: number): number {
  let quotient = n;
  let count = 0;

  while (quotient) {
    if (quotient % 2 === 1) count++;
    quotient = Math.floor(quotient / 2);
  }
  return count;
}
