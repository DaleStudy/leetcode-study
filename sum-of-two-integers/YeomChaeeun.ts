/**
 * 연산자 + 사용하지 않고 덧셈하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(logn) - 비트 수만큼 계산
 * - 공간 복잡도: O(1)
 * @param a
 * @param b
 */
function getSum(a: number, b: number): number {
    while(b !== 0) {
        let carry = a & b; // and - 11 & 10 = 10
        a = a ^ b; // xor - 11 ^ 10 = 01
        b = carry << 1; // 100
    }

    return a
}
