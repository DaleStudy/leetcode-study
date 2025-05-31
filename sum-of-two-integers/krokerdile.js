/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
function getSum(a, b) {
    while (b !== 0) {
        const sum = a ^ b;            // 자리올림 없는 합
        const carry = (a & b) << 1;   // 자리올림 비트

        a = sum;
        b = carry;
    }

    return a;
}
