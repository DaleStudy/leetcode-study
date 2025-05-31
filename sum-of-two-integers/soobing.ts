/**
 * 문제 설명
 * - 두 정수의 합을 반환하는 문제 (비트 연산을 통해서)
 *
 * 아이디어
 * - 반올림은 AND(&) + 왼쪽 shift 1, 덧셈은 XOR(^) 연산을 통해서 한다.
 * - 반올림이 0이 될 때까지 반복한다. ⭐️
 */
function getSum(a: number, b: number): number {
  while (b !== 0) {
    const carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
  }
  return a;
}
