/**
 *
 * @param a - 정수 a
 * @param b - 정수 b
 * @returns - 더하기 연산 없이 더한 값 반환
 * @description
 * - bit 연산이구나! 싶었는데 비트를 잘 다룰줄 몰라서 ai의 도움을 받음
 */

function getSum(a: number, b: number): number {
  while (b !== 0) {
    // 올림수 계산 : 둘다 1인 비트를 AND 연산으로 찾아 왼쪽으로 밈 (올림수니까)
    const carry = (a & b) << 1;

    // XOR 연산으로 올림수를 제외한 덧셈 값 도출 (1 | 0 이므로)
    a = a ^ b;

    b = carry;
  }

  return a;
}

const a = 2;
const b = 3;
getSum(a, b);


