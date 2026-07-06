/**
toString(2)으로 해결했다가 다른 분의 풀이를 보고 다시 풀어보았다.

'비트 연산을 통한 계산'이다.
컴퓨터에서 모든 언어는 2진법으로 변환이 되는데, 이를 이용한 플이다.
가장 오른쪽 비트가 1인 경우에 count++, n을 우측으로 1칸 shift.
shift를 하면 결국 남는 숫자는 0이기 때문에 적절한 조건으로 루프를 빠져나온다.

굳이 2진법으로 변환하지 않고도 계산할 수 있어서 이게 더 좋은 풀이라 생각하였다.
 */
/**
 * @param {number} n
 * @return {number}
 */
function hammingWeight(n) {
  let count = 0;

  while (n !== 0) {
    count += n & 1;
    n >>>= 1;
  }

  return count;
}
