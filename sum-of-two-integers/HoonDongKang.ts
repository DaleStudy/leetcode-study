/**
 * [Problem]: [371] Sum of Two Integers
 * (https://leetcode.com/problems/sum-of-two-integers/description/)
 */
function getSum(a: number, b: number): number {
    // 시간복잡도 O(n)
    // 공간복잡도 O(1)
    while (b !== 0) {
        const carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a;
}
