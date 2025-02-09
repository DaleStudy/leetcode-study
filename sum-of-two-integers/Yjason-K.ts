/**
 * +, - 기호를 사용하지 않고 두 정수의 합을 구하기
 * @param {number} a - 정수
 * @param {number} b - 정수
 * @return {number} - 두 정수의 합
 */
function getSum(a: number, b: number): number {
    // 1. XOR 연산으로 덧셈 처리
    // 2. AND 연산으로 올림 처리
    // 3. 올림이 없을 때까지 반복
    while (b !== 0) {
        const carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a;
}

