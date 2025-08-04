/*
 * 두 정수 a와 b가 주어졌을 때, + 와 - 연산자를 사용하지 않고 두 수의 합 구하기
 *
 * 접근 방법: 비트연산 / ALU 연산을 사용하여 두 수의 합을 구함
 * 1. XOR 연산을 사용하여 두 수의 합을 구함 (올림수는 제외)
 * 2. AND 연산과 왼쪽 시프트를 사용하여 올림수를 구함
 * 3. 위의 두 과정을 올림수가 0이 될 때까지 반복
 *
 * 시간복잡도: O(log max(a,b)), 최대 32번 반복
 * 공간복잡도: O(1)
 */
/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function (a, b) {
  while (b !== 0) {
    // XOR: 자리올림 없는 덧셈
    let sum = a ^ b;

    // AND + 시프트: 자리올림 계산
    let carry = (a & b) << 1;

    // 다음 반복을 위해 값 업데이트
    a = sum;
    b = carry;
  }

  return a;
};
