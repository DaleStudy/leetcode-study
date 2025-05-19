/**
 *
 * 문제 설명
 * - 32비트 unsigned 정수의 비트 순서를 뒤집어서 다시 정수로 반환하는 문제
 *
 * 아이디어
 * - 비트 연산을 이해하고, O(1)알아가는데 의의를 두면 좋을 것 같음.
 *
 * 비트 연산
 * >>>, >>, <<, &, |
 * - signed, unsigned 연산
 */
function reverseBits(n: number): number {
  let result = 0;
  for (let i = 0; i < 32; i++) {
    result <<= 1;
    result |= n & 1;
    n >>>= 1;
  }

  return result >>> 0;
}
